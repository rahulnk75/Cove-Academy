# Generated by Django 5.1.2 on 2025-01-27 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_groupchat_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='group',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.DeleteModel(
            name='GroupChat',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
