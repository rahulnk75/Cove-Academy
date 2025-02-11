# Generated by Django 5.1.2 on 2025-01-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseApp', '0021_group_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('sender_email', models.EmailField(max_length=200)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='group',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
