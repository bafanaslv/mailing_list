from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, related_name="clients", **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    def __str__(self):
        return f'{self.email} - {self.name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        permissions = [
            ("can_unpublish_product", 'Can unpublish product'),
            ("can_change_product_description", "Can change product description"),
            ("can_change_product_category", "Can change product category"),
        ]


class Message(models.Model):
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, related_name="messages", **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='заголовок')
    body = models.TextField(verbose_name='сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    STATUS = [("created", "создана"),
              ("started", "запущена"),
              ("completed", "завершена"),
              ("disabled", "отключена")]

    PERIODICITY = [("daily", "ежедневно"),
                   ("weekly", "еженедельно"),
                   ("monthly", "ежемесячно")]

    owner = models.ForeignKey(User, related_name='mailings', on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    message = models.ForeignKey(Message, related_name='messages', on_delete=models.CASCADE, verbose_name='сообщение')
    client = models.ManyToManyField(Client, related_name='client', verbose_name='клиент')
    begin_time = models.DateTimeField(verbose_name='дата и время первой отправки рассылки')
    end_time = models.DateTimeField(verbose_name='дата и время окончания отправки рассылок')
    periodicity = models.CharField(max_length=10, choices=PERIODICITY, default='ежедневно', verbose_name='периодичность')
    status = models.CharField(max_length=10, choices=STATUS, default='created', verbose_name='статус')

    def str(self):
        return f'Рассылка: {Client.name}, {Client.email} - {Message.title} {self.status}'

    def complete_mailing(self):
        self.actual_end_time = timezone.now()
        self.status = 'completed'
        self.save()

    def start_mailing(self):
        self.actual_start_time = timezone.now()
        self.status = 'started'
        self.save()

    class Meta:
        ordering = ['-begin_time']
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        permissions = [
            ("can_disabled_mailing", 'Can disabled mailing'),
        ]


class MailingAttempt(models.Model):
    STATUS = [('success', 'успешно'),
              ('failed', 'неудачно')]

    mailing = models.ForeignKey(Mailing, related_name='attempts', on_delete=models.CASCADE, verbose_name='рассылка')
    last_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    status = models.CharField(max_length=10, choices=STATUS, default='failed', verbose_name='статус попытки')
    response = models.TextField(**NULLABLE, verbose_name='ответ сервера')

    def str(self):
        return f'Попытка: {self.mailing} - {self.status}'

    class Meta:
        ordering = ['-last_time']
        verbose_name = 'попытка'
        verbose_name_plural = 'попытки'
