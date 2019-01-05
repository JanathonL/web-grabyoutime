from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phone_field import PhoneField

class UserLabel:
    MEMBER = 1
    MANAGER = 2
    typeChoice = (
        (MEMBER, 'member'),
        (MANAGER, 'manager'),
    )
    defaultChoice = MEMBER

class User(AbstractUser):
    user_type = models.SmallIntegerField(choices=UserLabel.typeChoice, default=UserLabel.defaultChoice, verbose_name='user type')
    mute_txt = models.BooleanField(default=False)
    mute_email= models.BooleanField(default=False)
    mute_inbox = models.BooleanField(default=False)
    #telephone = models.CharField(max_length = 11)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Group(models.Model):
    # primary key is the Group Id which is a explicit field
    title = models.CharField(max_length=42, verbose_name='Group Name') 
    detail = models.TextField(default="Nothing for this project...", blank=True, verbose_name='Group detail')
    # a group can only has a single manager
    manager = models.ForeignKey(User, verbose_name='manager', on_delete=models.CASCADE)
    # a group may has a lot of members
    members = models.ManyToManyField(User, related_name='added_groups', verbose_name='team member')

    # a group has a create date
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return '<Group: ' + self.title + ' own by ' +  self.manager + '>'
    
    class Meta:
        ordering = ('create_date', )

class GroupProjectStatus:
    CREATING = 1 
    FINISHED = 2
    ONGONING = 3  


class GroupProject(models.Model):
    STATUS = (
        (GroupProjectStatus.CREATING, 'Creating'), 
        (GroupProjectStatus.FINISHED, 'Finished'),  
        (GroupProjectStatus.ONGONING, 'ONGONING'), 
    )
    ## the name of the group project 
    name = models.CharField(max_length=100, verbose_name='Group name')

    ## the status of group project, finish, creating, ongoing..
    status = models.SmallIntegerField(choices=STATUS, default=GroupProjectStatus.CREATING, verbose_name='Group Status')

    ## detail intro for this project 
    detail = models.TextField(default="Nothing for this project...", blank=True, verbose_name='Project detail')

    ## which group this project belong to 
    belong = models.ForeignKey(Group, verbose_name='Group project', on_delete=models.CASCADE)

    ## the creator of this project 
    creator = models.ForeignKey(User, related_name='my_project', verbose_name='leader', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='added_groupprojects', verbose_name='team member')
    
    ## time field for this project 
    create_date = models.DateTimeField(auto_now_add=True)

    ## estimate time for this project 
    estimate_time = models.IntegerField(default=0, blank=True,null=True)

    start_date = models.DateTimeField(default=None, blank=True, null=True, verbose_name='Start Time')

    finish_date = models.DateTimeField(default=None, blank=True, null=True, verbose_name='End Time')


    spend_time = models.FloatField(default=0, blank=True,null=True)

    deadline = models.DateTimeField(default=None, blank=True,null=True, verbose_name='Deadline')

    ## whether this project has start or not.
    is_begin = models.BooleanField(default=False, blank = False) 

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

## the data model for the progress
## (progress, user, project, date) 
class Progress(models.Model):
    begin_time = models.DateTimeField(default=None, blank=True, null=True,  verbose_name='Begin Time')
    progress = models.FloatField(default=0, blank=True, verbose_name='Progress')
    date = models.DateTimeField(default=None, blank=True, verbose_name='Date')
    project = models.ForeignKey(GroupProject, verbose_name='Group project', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class InviteStatus:
    ACCEPT = 4
    REJECT = 5 
    INIT = 6

class Invite(models.Model):
    STATUS = (
        (InviteStatus.ACCEPT, 'ACCEPT'), 
        (InviteStatus.REJECT, 'REJECT'),  
        (InviteStatus.INIT, 'INIT'), 
    )
    manager = models.ForeignKey(User, related_name='manager', on_delete=models.CASCADE)
    member = models.ForeignKey(User, related_name='member', on_delete=models.CASCADE)
    join_id = models.IntegerField(blank=False)
    is_group = models.BooleanField(default=True, blank = False)
    is_join = models.BooleanField(default=True, blank = False)
    status = models.SmallIntegerField(choices=STATUS, default=InviteStatus.INIT, verbose_name='Invite Status')

    def __repr__(self):
        return '<Invite status: %d>' % (self.status)

    @staticmethod
    def generate(manager: User, member: User, is_group: bool, is_join: bool, join_id:join_id):
        invite = Invite.objects.create(manager=manager, member=member,
                              join_id=join_id, is_group=is_group, is_join=is_join)
        return invite.pk
    
    def join(self):
        obj = None
        obj = get_object_or_404(Group, pk=self.join_id) if self.is_group else get_object_or_404(GroupProject, pk=self.join_id)
        if self.can_join(obj):
            obj.members.add(self.member)
            self.status = InviteStatus.ACCEPT
            obj.save()
            self.save()

    def can_join(self, obj):
        if self.is_group:
            if obj in self.member.added_groups.all():
                return False
        else:
            if obj in self.member.added_groupprojects.all():
                return False
        return True
    
    def get_name_of_obj(self):
        obj = None
        if self.is_group:
            obj = get_object_or_404(Group, pk=self.join_id)
            return obj.title
        else:
            obj = get_object_or_404(GroupProject, pk=self.join_id)
            return obj.name

    def reject(self):
        self.status = InviteStatus.REJECT
        self.save()