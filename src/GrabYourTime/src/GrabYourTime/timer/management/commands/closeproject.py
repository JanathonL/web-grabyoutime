from django.core.management.base import BaseCommand, CommandError
from timer.models import *
import datetime  
from django.utils.timezone import utc
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib import messages
class Command(BaseCommand):
    help = 'close project on midnight'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for user_id in options['user_id']:
            try:
                user = User.objects.get(pk=user_id)
                username=user.username
                progresses = Progress.objects.filter(user__exact=user)
                self.stdout.write(self.style.SUCCESS('Successfully print user "%s"' % user))
                for item in progresses:
                    project = get_object_or_404(GroupProject, pk=item.project.id)
                    project.is_begin = False
                    project.save()
                    today = datetime.date.today()
                    progress = Progress.objects.filter(date__exact=today, project=project, user=user)
                    if progress: 
                        progress = progress[0]
                        now = datetime.datetime.utcnow().replace(tzinfo=utc)
                        timediff = now - progress.begin_time
                        if progress.begin_time is None:
                            self.stdout.write(self.style.SUCCESS('Stop project "%s" failed! begin_time is None' % user))
                        
                        print("total progress:",progress.progress)
                        progress.progress += timediff.seconds / 3600.0
                        print("progress:",timediff.seconds / 3600.0)
                        progress.save()
                        self.stdout.write(self.style.SUCCESS('Stop project "%s"sucessfully! ' % user))
                    else:
                        self.stdout.write(self.style.SUCCESS('Stop project "%s" failed! You have not beginned doing project' % user))
                self.stdout.write(self.style.SUCCESS('Successfully print user "%s"' % user))
            except User.DoesNotExist:
                raise CommandError('USER "%s" does not exist' % user_id)
           