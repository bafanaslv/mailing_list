# Generated by Django 5.0.6 on 2024-07-31 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_mailing_attempts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='attempts',
        ),
    ]
