# Generated by Django 4.0.1 on 2022-01-28 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_user_voca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_voca',
            new_name='finished_voca',
        ),
        migrations.RemoveField(
            model_name='user',
            name='finished_collection',
        ),
        migrations.RemoveField(
            model_name='user',
            name='finished_collection_voca',
        ),
        migrations.RemoveField(
            model_name='user',
            name='finished_user_voca',
        ),
    ]
