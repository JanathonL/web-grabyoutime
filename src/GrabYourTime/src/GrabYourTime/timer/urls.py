from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from timer.views import *
import notifications.urls

urlpatterns = [
    url(r'^$', auth_views.LoginView.as_view(template_name='login.html')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'dashboard/', dashboard, name="dashboard"),
    #url(r'home/', home, name="home"),
    url(r'inbox/', inbox, name="inbox"),
    #url(r'note/', note, name="note"),
    url(r'editprofile/',edit_profile, name = "editprofile"),
    url(r'calendar/', calendar, name="calendar"),
    #url(r'profile/', profile, name="profile"),
    url(r'mute_txt/', mute_txt, name="mute_txt"),
    url(r'mute_email/', mute_email, name="mute_email"),
    url(r'mute_inbox/', mute_txt, name="mute_inbox"),

    url(r'^$', login, name='start'),
    url(r'^login/$', login, name='login'),
    url(r'logout/', auth_views.LogoutView.as_view(next_page='/login/'), name="logout"),
    url(r'signup/', signup, name="signup"),
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name="activate"),
    url(r'^password/reset/$', 
        auth_views.PasswordResetView.as_view(template_name='password_reset.html', 
        success_url='/password/reset/done/', email_template_name='password_reset_email_template.html'), 
        name="password_reset"),
    url(r'^password/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name="password_reset_done"),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', success_url='/password/done/'),
        name="password_reset_confirm"),
    url(r'^password/done/$', 
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name="password_reset_complete"),
    #url(r'grouppage/', group_page, name="grouppage"),

    # user
    url(r'^users/(\w+)/$', user_detail, name='user_detail'),

   
    # group part 
    # list all the groups
    url(r'^groups$', groups, name='list'),
    # list the detail of a spefic group
    url(r'^(\d+)/$', group_detail, name='detail'),
    url(r'^create_group/$', group_create, name ='creategroup'),

    # project part url
    url(r'^projects/', include([
        url(r'^begin/(?P<project_id>\d+)/(?P<user_id>\d+)/$', begin_project, name='begin_project'),
        url(r'^finish/(?P<project_id>\d+)/(?P<user_id>\d+)/$', finish_project, name='finish_project'),
        url(r'^stop/(?P<project_id>\d+)/(?P<user_id>\d+)/$', stop_project, name='stop_project'),
        url(r'^create/(\d+)/$', create_project, name='create_project'),
        url(r'^(\d+)/$', project_detail, name='project_detail'),
        url(r'^$', projects, name='projects')
    ]), name='project'),

    url(r'^invite/', include([
        url(r'^join_group/(\d+)$', join_group, name='join_group'),
        url(r'^accept_join_group/(.*)$', accept_join_group, name='accept_join_group'),
        url(r'^rej_join_group/(.*)$', rej_join_group, name='rej_join_group'),
        url(r'^join_project/(\d+)$', join_project, name='join_project'),
        url(r'^accept_join_project/(.*)$', accept_join_project, name='accept_join_project'),
        url(r'^rej_join_project/(.*)$', rej_join_project, name='rej_join_project'),
    ])),

    # get number of msg
    url(r'^get_message/$', get_message, name='get_message'),

    # setting part
    url(r'setting/', setting, name ="setting"),
    #url(r'group_setting/', group_setting, name ="group_setting"),
    #url(r'notification_setting/', notification_setting, name = "notification_setting"),
    #url(r'member_setting/', member_setting, name = "member_setting"),
    #url(r'project_setting/', project_setting, name = "project_setting"),
    url(r'get_events/', get_events, name="get_events") ,
]