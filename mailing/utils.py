import logging
import smtplib
from django.utils import timezone
import pytz

from blogs.models import Blog
from mailing.models import Mailing, MailingAttempt, Client
from django.core.mail import send_mail
from django.conf import settings


logger = logging.getLogger('mailing')


def send_mailings():
    now = timezone.now()
    msk_time = now.astimezone(pytz.timezone(settings.TIME_ZONE))
    mailings = Mailing.objects.filter(status__in=['created', 'started'])
    logger.debug(f'Найдено {mailings.count()} рассылок для обработки.')

    for mailing in mailings:
        if mailing.status == 'completed':
            logger.debug(f'Рассылка {mailing.id} уже завершена.')
            continue

        if mailing.status == 'created':
            if should_send_mailing(mailing, msk_time):
                send_mailing(mailing)
        elif mailing.status == 'started':
            if mailing.end_time and mailing.end_time <= msk_time:
                mailing.complete_mailing()
            elif should_send_mailing(mailing, msk_time):
                send_mailing(mailing)


def should_send_mailing(mailing, now):
    last_attempt = mailing.attempts.order_by('-last_time').first()
    if not last_attempt:
        return True

    last_attempt_timestamp_msk = last_attempt.last_time.astimezone(pytz.timezone(settings.TIME_ZONE))
    delta = now - last_attempt_timestamp_msk
    logger.debug(f'Последняя попытка рассылки {mailing.message}: {last_attempt_timestamp_msk}, {delta.days} дней назад.')
    if mailing.periodicity == 'daily' and delta.days >= 1:
        return True
    elif mailing.periodicity == 'weekly' and delta.days >= 7:
        return True
    elif mailing.periodicity == 'monthly' and delta.days >= 30:
        return True
    return False


def send_mailing(mailing):
    recipients = mailing.client.all()
    title = mailing.message.title
    body = mailing.message.body
    clients_list = []
    for client in recipients:
        clients_list.append(client.email)
    try:
        # Отправляем письмо
        server_response = send_mail(
            subject=title,
            message=body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=clients_list,
            fail_silently=False,
        )
        status = 'success'
        logger.info(f'Письмо успешно отправлено клиентам {clients_list} для рассылки {mailing.message}.')
    except smtplib.SMTPException as error:
        # При ошибке почтового сервера получаем ответ - ошибка, которая записывается в error
        server_response = str(error)
        status = 'failed'
        logger.error(f'Ошибка при отправке письма {clients_list} для рассылки {mailing.message}: {server_response}')

        # Записываем попытку рассылки
    MailingAttempt.objects.create(
        mailing=mailing,
        status=status,
        response=server_response
    )

    mailing.start_mailing()
    logger.info(f'Рассылка {mailing.message} начата.')


class ContextMixin:
    """ Миксин для вывода статистики и блогов в гравной странице."""
    def get_main_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_mailing"] = Mailing.objects.all().count()
        context["count_mailing_enabled"] = Mailing.objects.filter(status__in=['created', 'started']).count()
        context["unique_users"] = len(Client.objects.values_list("email").distinct())
        context["blog_list"] = Blog.objects.order_by('?').all()[:3]
        return context


if __name__ == "__main__":
    send_mailings()
