# Generated by Django 4.2.2 on 2024-08-10 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'permissions': [('can_unpublish_product', 'Can unpublish product'), ('can_change_product_description', 'Can change product description'), ('can_change_product_category', 'Can change product category')], 'verbose_name': 'клиент', 'verbose_name_plural': 'клиенты'},
        ),
        migrations.AlterModelOptions(
            name='mailing',
            options={'ordering': ['-begin_time'], 'permissions': [('can_disabled_mailing', 'Can disabled mailing')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
    ]
