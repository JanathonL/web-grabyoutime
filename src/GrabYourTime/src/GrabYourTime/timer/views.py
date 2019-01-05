from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from timer.forms import *
from notifications.signals import notify
from notifications.models import Notification
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http import Http404, HttpResponse
from django.contrib.auth import update_session_auth_hash
from mimetypes import guess_type
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from collections import defaultdict
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core import serializers
import datetime  
from .models import * 
from django.utils.timezone import utc
from django.db.models import Q

# Create your views here.
#def group_page(request):
#    return render(request, 'groups.html', context={})

def setting(request):
    return render(request, 'setting.html', context={})

#def group_setting(request):
#    return render(request, 'group_setting.html', context={})

#def member_setting(request):
#    return render(request, 'member_setting.html', context={})

#def notification_setting(request):
#    return render(request, 'notification_setting.html', context={})

#def project_setting(request):
#    return render(request, 'project_setting.html', context={})

def countOngoingProgress(item):
    pro = GroupProject.objects.get(id=item.project.id)
    if pro.is_begin:
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        timediff = now - item.begin_time
        if item.begin_time is None:
            messages.warning(request, 'Collect data for {project} failed! begin_time is None'.format(project=pro.name))
            return redirect('project_detail', pro.pk) 
        return timediff.seconds / 3600
    else:
        return 0

def dashboard(request):
    # year_data  [12,] list
    # week_data  [7,]  list
    # project label and data
    # "Todo", "Attempted", "Solved"  table data

    context = {}
    
    progresses = Progress.objects.filter(user__exact=request.user)
    Solved_set = set()
    Attempted_set = set()
    Todo_set = set()
    for item in progresses:
        pro = GroupProject.objects.get(id=item.project.id)
        if pro.finish_date is not None:
            Solved_set.add(pro.id)
        elif pro.start_date is None:
            Todo_set.add(pro.id)
        else:
            Attempted_set.add(pro.id)
    Solved_num = len(Solved_set)
    Todo_num = len(Todo_set)
    attempted_num = len(Attempted_set)
    context['table_data'] = [Todo_num, attempted_num, Solved_num]

    # project label and data
    project_label_set = defaultdict(int)
    for item in progresses:
        pro = GroupProject.objects.get(id=item.project.id)
        project_label_set[pro.name] += countOngoingProgress(item)
        project_label_set[pro.name] += item.progress
    project_label_set = sorted(project_label_set.items(), key = lambda x:x[1], reverse = True)[:5][::-1]
    project_label = []
    project_data = []
    for key, val in project_label_set:
        project_label.append(key)
        project_data.append(val)
    print(project_label)
    context['project_label'] = project_label
    context['project_data'] = project_data
 
    context['project_data_max'] = max(max(project_data), 1) if len(project_data) != 0 else 1

    week_index = datetime.datetime.now().weekday()
    week_info = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_data = [] 
    week_label = []
    for i in range(7):
        now = datetime.datetime.now()
        time = now + datetime.timedelta(days=-i)
        time = time.date()
        value = 0
        for item in progresses:
            print("time:{}, item.date:{}".format(time, item.date))
            if item.date.year == time.year and item.date.day == time.day and item.date.month == time.month:
                value += countOngoingProgress(item)
                value += item.progress
        index = time.weekday()
        week_label.append(week_info[index])
        week_data.append(value)
    #print(week_data)
    context['week_data'] = week_data[::-1]
    context['week_label'] = week_label[::-1]
    context['week_data_max'] = max(max(week_data[::-1]) * 2, 1) if len(week_data) != 0 else 1

    year_info = ["","Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    year_data = []
    year_label = []
    now = datetime.datetime.now()
    curmon = now.month
    curyear = now.year 
    for i in range(12):
        #print(curmon)
        #print(year_info[curmon])
        #print(curyear)
        value = 0
        for item in progresses:
            if item.date.month == curmon and item.date.year == curyear:
                value += countOngoingProgress(item)
                value += item.progress
        year_data.append(value)
        year_label.append(year_info[curmon])
        curmon -= 1
        if curmon <= 0:
            curmon += 12
            curyear -= 1
    #print(year_data)
    #print(year_label)
    max_data = int(max(year_data) + 1)
    if max_data % 2 is not 0:
        max_data += 1 
    context['year_data'] = year_data[::-1]
    context['year_label'] = year_label[::-1]
    context['max_data'] = max_data
    context['time'] = datetime.datetime.now()
    return render(request,"dashboard.html",context)

'''def home(request):
    context = {}
    errors = []
    context['errors'] =errors
    context['userid'] = int(request.user.id)
    return render(request, 'home.html', context)'''

@login_required
def calendar(request):
    return render(request, 'calendar.html', context={})

@login_required
def get_events(request):
    events = []
    user = request.user
    projects = user.added_groupprojects.all()
    for project in projects:
        event = {}
        event['title'] = project.name
        event['start'] = str(project.deadline.strftime('%Y-%m-%d'))
        event['url'] = reverse('project_detail', args=(project.id,))
        events.append(event)
    #print(events)
    context = {'events':events}
    return render(request, 'events.json', context, content_type='application/json')

@login_required
def inbox(request):
    context={}
    queryset = request.user.notifications
    memberset = Group.objects.all()
    query = request.GET.get('query') or None
    if query:
        memberset = memberset.filter(title__contains=query)
    in_groups = request.user.added_groups.all()
    p = Paginator(memberset, 5)
    page = request.GET.get('page') or 1
    try:
        group_list = p.page(page)
    except PageNotAnInteger:
        group_list = p.page(1)
    except EmptyPage:
        group_list = p.page(p.num_pages)
    context['p'] = group_list
    context['query'] =query
    context['in_groups'] = in_groups
    context['current_user'] = request.user
    context['notifications'] =queryset
    return render(request, 'inbox.html', context)

#def note(request):
#    return render(request, 'notes.html', context={})

####To do #######
##this is used for view profile only
'''def profile(request):
    context = {}
    errors = []
    context['errors'] =errors
    context['userid'] = int(request.user.id)
    print("view profile")
    return render(request, 'viewprofile.html', context)'''

@login_required
def edit_profile(request):
    context = {}
    #Find the user
    user = User.objects.get(username = request.user.username)
    context['userid'] = int(request.user.id)
    if(request.method == "GET"):
        context['form'] = ProfileForm(instance = user)
        return render(request, 'editprofile.html', context)
    # items Sorting
    form = ProfileForm(request.POST, request.FILES, instance = user)
    context['form'] = form
    if not form.is_valid():
        return render(request, 'editprofile.html', context)
    form.save()
    messages.success(request, 'update profile successfully')
    return render(request, 'editprofile.html', context)

def signup(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = False
            new_user.mute=False
            new_user.save()
            # sending email
            # get current sit
            site = get_current_site(request)
            subject = 'Verify your email address'
            from_mail = 'yaxil@andrew.cmu.edu'
            to_mail = form.cleaned_data['email']
            # use a email template
            email_body = render_to_string('acc_mail_template.html', {
                'user': new_user,
                'domain': site.domain,
                # reference: https://docs.djangoproject.com/en/2.0/releases/2.0/#removed-support-for-bytestrings-in-some-places
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)).decode(),
                'token': default_token_generator.make_token(new_user),
            })
            send_mail(subject=subject, message=email_body, from_email=from_mail, recipient_list=[to_mail])
            sendMsgSuccess(request, 'welcome, '+ form.cleaned_data['username'] + '! A verification email has been sent to ' + to_mail)
            context = {'form': RegForm()}
            return render(request, 'signup.html', context=context)
        else:
            context = {'form': form}
            print([item for msg, item in form.error_messages.items()])
            errors = " ".join([str(item) for msg, item in form.error_messages.items()])
            sendMsgError(request, 'Register fail! '+ errors)
            return render(request, 'signup.html', context=context)
    else:
        form = RegForm()
    return render(request, 'signup.html', context={'form': form})

def sendMsgWarning(request, msg):
    messages.warning(request, msg)

def sendMsgSuccess(request, msg):
    messages.success(request, msg)

def sendMsgError(request, msg):
    messages.error(request, msg)

def login(request):
    if request.user.is_authenticated:
        sendMsgWarning(request, request.user.username + ' , you have logged in')
        return redirect('dashboard')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            check = auth.authenticate(username=username, password=password)
            if check:
                auth.login(request, check)
                sendMsgSuccess(request, 'Welcome, '  + request.user.username
                +'. If you are new here, please check Help Center ( on your left bar) for more information.')
                return redirect('dashboard')
            else:
                sendMsgError(request, 'Invalid Login Info')
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})

# new user activate
def activate(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    request_user = get_object_or_404(User, pk=uid)
    # user.is_active can't be true 
    if default_token_generator.check_token(request_user, token) and not request_user.is_active:
        request_user.is_active = True
        request_user.save()
        return render(request, 'active_message.html', context={'active':True})
    else:
        return render(request, 'active_message.html', context={'active':False})


@login_required
def user_detail(request, username):
    msg_form = MessageForm(request.POST or None)
    user = get_object_or_404(User, username=username)
    if request.user.is_authenticated and msg_form.is_valid():
        notify.send(request.user, recipient=user, verb='send you a message',
                    description=msg_form.cleaned_data.get('content', None))
        messages.success(request, 'send a message successfully')
        return redirect('user_detail', username)
    joined_projects = [project for project in user.added_groupprojects.all()]
    joined_group = [group for group in user.added_groups.all()]
    print(joined_projects)
    context = {}
    context['user'] = user
    context['groups'] = joined_group
    context['projects'] = joined_projects
    return render(request, 'user_detail.html', context)

## group part
@login_required
def group_create(request):
    if request.method == 'POST':
        user = User.objects.get(username__exact=request.user.username)
        group = Group.objects.create(manager=user)
        group.members.add(user)
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            print("form is not valid")
            context = {'form': form}
            return render(request, 'create_group.html', context=context)
    else:
        form = GroupForm()
    return render(request, 'create_group.html', context={'form': form})

@login_required
def groups(request):
    queryset = Group.objects.all()
    query = request.GET.get('query') or None
    if query:
        queryset = queryset.filter(title__contains=query)
    in_groups = request.user.added_groups.all()
    p = Paginator(queryset, 5)
    page = request.GET.get('page') or 1
    try:
        group_list = p.page(page)
    except PageNotAnInteger:
        group_list = p.page(1)
    except EmptyPage:
        group_list = p.page(p.num_pages)
    return render(request, 'groups.html', {
        'p': group_list,
        'query': query,
        'in_groups': in_groups,
        'current_user': request.user,
    })

@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    in_group = group in request.user.added_groups.all()
    project_for_current_user = request.user.added_groupprojects.filter(belong=group)
    print(request.user.user_type)
    return render(request, 'group_detail.html', {
        'group': group,
        'in_projects': project_for_current_user,
        'projects': group.groupproject_set.all(),
        'is_author_manager': group.manager == request.user,
        'in_group':in_group,
    })

# project part 
@login_required
def create_project(request, project_id):
    print("create_project:",project_id)
    group = get_object_or_404(Group, pk=project_id)
    if request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid():
            
            project = form.save(commit=False)
            project.creator = request.user
            project.belong = group
            project.is_begin = False
            project.save()

            project.members.add(request.user)
            messages.success(request, 'create project successfully')
            return redirect('projects')
        else:
            print("form is not valid")
            context = {'form': form, 'group':group}
            return render(request, 'project_create.html', context=context)
    else:
        form = ProjectForm()
        context = {'form': form, 'group':group}
        return render(request, 'project_create.html', context=context)

@login_required
def projects(request):
    queryset = GroupProject.objects.all()
    query = request.GET.get('query', None)
    group_id = request.GET.get('group', None)
    params = {}
    if query:
        params['query'] = query
        queryset = queryset.filter(name__contains=query)
    elif group_id:
        params['group'] = get_object_or_404(Group, pk=group_id)
        queryset = queryset.filter(belong=params['group'])
    p = Paginator(queryset, 5)
    page = request.GET.get('page') or 1
    try:
        params['p'] = p.page(page)
    except PageNotAnInteger:
        params['p'] = p.page(1)
    except EmptyPage:
        params['p'] = p.page(p.num_pages)
    return render(request, 'projects.html', params)

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(GroupProject, pk=project_id)
    today = datetime.date.today()
    progress = Progress.objects.filter(date__exact=today, project=project, user=request.user)
    print(len(progress))
    context = {}
    context['project'] = project
    if progress:
        context['begin_time'] = str(progress[0].begin_time) 
    else:
        context['begin_time'] = None
    print(context['begin_time'])
    context['user_id'] = request.user.id
    context['in_project'] = project in request.user.added_groupprojects.all()
    return render(request, 'project_detail.html', context)


@login_required
def begin_project(request, project_id, user_id):
    project = get_object_or_404(GroupProject, pk=project_id)
    project.is_begin = True
    project.save()
    today = datetime.date.today()
    progress = Progress.objects.filter(date__exact=today, project=project, user=request.user)
    if progress:
        progress = progress[0]
        progress.begin_time = datetime.datetime.now()
        print("begin time is ")
        print(progress.begin_time)
        progress.save()
        messages.success(request, 'begin project {project} sucessfully!'.format(project=project.name))
    else:
        print("????")
        progress = Progress.objects.create(date=today, project=project,user=request.user, 
            progress=0, begin_time=datetime.datetime.now())
        if project.start_date is None:
            project.start_date = today
            project.save()
        messages.success(request, 'begin project {project} sucessfully!'.format(project=project.name))

    return redirect('project_detail', project.pk) 

@login_required
def stop_project(request, project_id, user_id):
    project = get_object_or_404(GroupProject, pk=project_id)
    project.is_begin = False
    project.save()
    today = datetime.date.today()
    progress = Progress.objects.filter(date__exact=today, project=project, user=request.user)
    if progress: 
        progress = progress[0]
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        timediff = now - progress.begin_time
        if progress.begin_time is None:
            messages.warning(request, 'Stop project {project} failed! begin_time is None'.format(project=project.name))
            return redirect('project_detail', project.pk) 
        print("total progress:",progress.progress)
        progress.progress += timediff.seconds / 3600.0
        print("progress:",timediff.seconds / 3600.0)
        progress.save()
        messages.success(request, 'stop project {project} sucessfully!'.format(project=project.name))
    else:
        messages.warning(request, 'Stop project {project} failed! You have not beginned doing project'.format(project=project.name))

    return redirect('project_detail', project.pk) 


@login_required
def finish_project(request, project_id, user_id):
    today = datetime.date.today()
    project = get_object_or_404(GroupProject, pk=project_id)
    project.is_begin = False
    project.finish_date = today
    progresses = Progress.objects.filter(project=project)
    spend_time = 0.0

    for progress in progresses:
        print("spend time progress:",progress.progress)
        spend_time += progress.progress
    project.spend_time = spend_time
    project.save()
    messages.success(request, 'finish project {project} sucessfully!'.format(project=project.name))
    return redirect('project_detail', project.pk) 

def accept_join(str_code):
    invite_id = int(str_code.split(":")[1])
    invite = get_object_or_404(Invite, pk=invite_id)
    notification = get_object_or_404(Notification, recipient=invite.manager, description=str_code)
    notification.mark_as_read()
    invite.join()
    return invite


def reject_join(str_code):
    invite_id = int(str_code.split(":")[1])
    invite = get_object_or_404(Invite, pk=invite_id)
    notification = get_object_or_404(Notification, recipient=invite.manager, description=str_code)
    notification.mark_as_read()

    invite.reject()
    return invite

@login_required
def join_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    invite_id = Invite.generate(manager=group.manager, member=request.user,
                                          is_group=True, is_join=True, join_id=group_id)
    print(invite_id)
    notify.send(request.user, recipient=group.manager,
        verb='want to join <a href="/{g_id}/" target="_blank">{group}</a>'
        .format(group=group.title, g_id=group.pk), target=group, description="join group:{}".format(invite_id))
    messages.success(request, 'join group {group} sucessfully!'.format(group=group.title))
    return redirect('detail', group.pk)

@login_required
def accept_join_group(request, str_code: str):
    invite = accept_join(str_code)
    messages.success(request, '{username} join {group_name} accept'.format(username=invite.member.username, group_name=invite.get_name_of_obj()))
    return redirect('inbox')

@login_required
def rej_join_group(request, str_code: str):
    invite = reject_join(str_code)
    messages.warning(request, '{username} join {group_name} rejected'.format(username=invite.member.username ,group_name=invite.get_name_of_obj()))
    return redirect('inbox')

@login_required
def join_project(request, project_id):
    project = get_object_or_404(GroupProject, pk=project_id)

    invite_id = Invite.generate(manager=project.creator, member=request.user,
                                          is_group=False, is_join=True, join_id=project_id)
    notify.send(request.user, recipient=project.creator,
        verb='want to join <a href="/{p_id}/" target="_blank">{project}</a>'
        .format(project=project.name, p_id=project.pk), target=project, description="join project:{}".format(invite_id))
    messages.success(request, 'join project {project} sucessfully!'.format(project=project.name))
    return redirect('project_detail', project.pk)

@login_required
def accept_join_project(request, str_code: str):
    invite = accept_join(str_code)
    messages.success(request, '{username} join {project} accept'.format(username=invite.member.username, project=invite.get_name_of_obj()))
    return redirect('inbox')

@login_required
def rej_join_project(request, str_code: str):
    invite = reject_join(str_code)
    messages.warning(request, '{username} join {project} rejected'.format(username=invite.member.username ,project=invite.get_name_of_obj()))
    return redirect('inbox')


@login_required
def get_message(request):
    size = len(request.user.notifications.unread())
    context = {"number":size}
    return render(request, 'msg_number.json', context, content_type='application/json')

#mute txt
@login_required
def mute_txt(request):
    user=request.user
    user.mute_txt= not user.mute_txt
    user.save()
    print (user.mute_txt)
    messages.warning(request, 'You have successfully change your SMS notification')
    return redirect('editprofile')
    
#mute email
@login_required
def mute_email(request):
    user=request.user
    user.mute_email= not user.mute_email
    user.save()
    print (user.mute_email)
    messages.warning(request, 'You have successfully change your email notification')
    return redirect('editprofile')

@login_required
def mute_inbox(request):
    user=request.user
    user.mute_txt= not user.mute_txt
    user.save()
    print ("mute inbox ....")
    messages.warning(request, 'You have successfully change your inbox notification')
    return redirect('editprofile')
