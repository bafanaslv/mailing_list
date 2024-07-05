from django.contrib import admin
from mailing.models import Message, Client, Mailing, MailingList, MailingAttempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "comment")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "body", "created_at")


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("id", "first_time", "periodicity", "status")


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ("id", "mailing", "client", "message")


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ("id", "mailing", "last_time", "status", "response", "email")
