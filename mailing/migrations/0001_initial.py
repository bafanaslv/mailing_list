# Generated by Django 5.0.6 on 2024-07-06 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиен',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('body', models.TextField(verbose_name='сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_time', models.DateTimeField(verbose_name='дата и время первой отправки рассылки')),
                ('end_time', models.DateTimeField(verbose_name='дата и время окончания отправки рассылок')),
                ('periodicity', models.CharField(choices=[('daily', 'ежедневно'), ('weekly', 'еженедельно'), ('monthly', 'ежемесячно')], default='daily', max_length=10, verbose_name='периодичность')),
            ],
            options={
                'verbose_name': 'настройка',
                'verbose_name_plural': 'настройки',
                'ordering': ['-begin_time'],
            },
        ),
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'создана'), ('started', 'запущена'), ('completed', 'завершена')], default='created', max_length=10, verbose_name='статус')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='mailing.client', verbose_name='клиент')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='mailing.message', verbose_name='сообщение')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='mailing.settings', verbose_name='настройка')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_time', models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')),
                ('status', models.CharField(choices=[('success', 'успешно'), ('failed', 'неудачно')], default='failed', max_length=10, verbose_name='статус попытки')),
                ('response', models.TextField(blank=True, null=True, verbose_name='ответ сервера')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='почта')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempts', to='mailing.mailinglist', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'попытка',
                'verbose_name_plural': 'попытки',
                'ordering': ['-last_time'],
            },
        ),
    ]
