# Generated by Django 4.2.2 on 2024-08-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('body', models.TextField(verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, help_text='загрузите изображение', null=True, upload_to='mailing/media', verbose_name='изображение')),
                ('view_counter', models.PositiveIntegerField(default=0, help_text='укажите количество просмотров', verbose_name='счетчик проcмотров')),
                ('data_publish', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
