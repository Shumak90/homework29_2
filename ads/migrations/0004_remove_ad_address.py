# Generated by Django 4.1 on 2022-08-18 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ad_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='address',
        ),
    ]