from django.contrib import admin
from mailing.models import Message, MailingList, MailingAttempt, Settings, Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "comment")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "body", "created_at")


@admin.register(Settings)
class SettingAdmin(admin.ModelAdmin):
    list_display = ("id", "begin_time", "end_time", "periodicity")


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ("id", "message", "setting", "client", "status")


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ("id", "mailing", "last_time", "status", "response", "email")
