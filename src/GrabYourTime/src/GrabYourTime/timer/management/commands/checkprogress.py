from django.core.management.base import BaseCommand, CommandError
from timer.models import *
import datetime  
from django.utils.timezone import utc
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from notifications.signals import notify

import json
from math import ceil

from twilio.base import values
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from twilio.rest import TwilioRestClient
class Command(BaseCommand):
    help = 'print user'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for user_id in options['user_id']:
            try:
                user = User.objects.get(pk=user_id)
                # user.mute=False
                print(user.username)

                username=user.username
                progresses = Progress.objects.filter(user__exact=user)
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
                print(Solved_num)
                print(Todo_num)
                print(attempted_num)
                #should be todo_num
                for i in range(Todo_num + attempted_num+ 1):
                    now = datetime.datetime.now() 
                    time = now + datetime.timedelta(days=-i * 30)
                    #print(time)
                    for item in progresses:
                        #send email
                            'domain': site,
                            # reference: https://docs.djangoproject.com/en/2.0/releases/2.0/#removed-support-for-bytestrings-in-some-places
                            'uid': urlsafe_base64_encode(force_bytes(user_id)).decode(),
                            'token': default_token_generator.make_token(user),
                        })
                        #print(email_body)
                        if(user.mute_email !=True):
                            send_mail(subject=subject, message=email_body, from_email=from_mail, recipient_list=[to_mail])
                        
                        # send inbox msgs
                        if(user.mute_inbox != True):
                            notify.send(user, recipient=user, verb='remind you have deadline today',
                                description=None)

                        #send text msgs
                        # Your Account SID from twilio.com/console
                        account_sid = "ACf189908875e4874cfaf2eb9c54a9ddd8"
                        # Your Auth Token from twilio.com/console
                        auth_token  = "a5a953bfce441f3fe2b01b3bd842eefa"

                        client = Client(account_sid, auth_token)
                        print(user.mute_txt)
                        # user.mute_txt=False
                        
                        phone = "+1"
                        temp = str(user.phone)
                        print(temp)
                        for i in range(len(temp)):
                            v = temp[i]
                            if v>='0' and v<='9':
                                phone += v

                        print(phone)

                        msg = "Don't forget your project:{} deadline is today!  From Timer team.".format(item.project.name)
                        if(user.mute_txt!=True):
                            try:
                                client.api.account.messages.create(
                                    to=phone, 
                                    from_="+17243052567",
                                    body=msg)
                            except TwilioRestException as ex:
                                print(ex)

                        
            except User.DoesNotExist:
                raise CommandError('USER "%s" does not exist' % user_id)
           