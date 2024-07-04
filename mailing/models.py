from django.db import models

NULLABLE = {'blank': True, 'null': True}


class MailingAddress(models.Model):
    email_address = models.EmailField(
        max_length=100,
        verbose_name='E-mail',
        help_text='введите адрес'
    )
    full_name = models.CharField(
        max_length=50,
        verbose_name='ФИО',
        help_text='введите ФИО клиента'
    )
    comment = models.TextField(
        **NULLABLE,
        verbose_name='комментарий'
    )

    def __str__(self):
        return f'{self.email_address} - {self.full_name}'

    class Meta:
        verbose_name = 'Адрес рассылки'
        verbose_name_plural = 'Адрес рассылки'


class Message(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='заголовок'
    )
    body = models.TextField(
        verbose_name='сообщение'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='создано'
    )

    def __str__(self):
        return f'{self.title}'

    class Metta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingList(models.Model):
    mailing_address = models.ForeignKey(
        MailingAddress,
        on_delete=models.PROTECT,
    )
    messages = models.ManyToManyField(
        Message, verbose_name=''
    )