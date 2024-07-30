from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from mailing.models import Log, Mailing


def send_mailing(mailing):
    now = timezone.localtime(timezone.now())
    if mailing.start_date <= now <= mailing.end_date:
        for message in mailing.messages.all():
            for client in mailing.clients.all():
                try:
                    result = send_mail(
                        subject=message.title,
                        message=message.text,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                        fail_silently=False
                    )
                    log = Log.objects.create(
                        time=mailing.start_date,
                        status=result,
                        server_response='success',
                        mailing_list=mailing,
                        client=client
                    )
                    log.save()
                    return log
                except SMTPException as e:
                    log = Log.objects.create(
                        time=mailing.start_date,
                        status=False,
                        server_response=e,
                        mailing_list=mailing,
                        client=client
                    )
                    log.save()
                    return log
    else:
        mailing.status = Mailing.COMPLETED


def ssss():
    """test"""
    send_mail(
        'Test Subject',
        'Test message body',
        # 'paravozishe@internet.ru',
        'masamunoff@yandex.ru',
        ['dobiultimate@gmail.com'],
        fail_silently=False,
    )


if __name__ == '__main__':
    ssss()