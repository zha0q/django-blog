# Generated by Django 3.2.5 on 2021-07-13 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='c_content',
        ),
    ]