# Generated by Django 4.0.1 on 2022-01-29 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_user_voca_user_finished_voca_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
    ]
