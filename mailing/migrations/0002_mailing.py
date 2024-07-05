# Generated by Django 5.0.6 on 2024-07-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_time', models.DateTimeField(verbose_name='дата и время первой отправки рассылки')),
                ('periodicity', models.CharField(choices=[('daily', 'ежедневно'), ('weekly', 'еженедельно'), ('monthly', 'ежемесячно')], default='daily', max_length=10, verbose_name='периодичность')),
                ('status', models.CharField(choices=[('created', 'создана'), ('started', 'запущена'), ('completed', 'завершена')], default='created', max_length=10, verbose_name='статус')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
                'ordering': ['-first_time'],
            },
        ),
    ]
