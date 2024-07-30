from mailing.services import send_mailing, ssss
from mailing.models import Mailing

ssss()
def daily_tasks():
    mailings = Mailing.objects.filter(periodicity="Раз в день", status="Запущена")
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)


def weekly_tasks():
    mailings = Mailing.objects.filter(periodicity="Раз в неделю", status="Запущена")
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)


def monthly_tasks():
    mailings = Mailing.objects.filter(periodicity="Раз в месяц", status="Запущена")
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)