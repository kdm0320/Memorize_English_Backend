# Generated by Django 4.0.1 on 2022-01-31 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qnaBoards', '0003_alter_qnaboard_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qnaboard',
            name='photo',
        ),
    ]