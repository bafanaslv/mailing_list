from django.core.management.base import BaseCommand
from mailing.utils import send_mailings


class Command(BaseCommand):
    help = 'check and send'

    def handle(self, *args, **kwargs):
        send_mailings()
        self.stdout.write(self.style.SUCCESS('Successfully checked and send mailings'))
