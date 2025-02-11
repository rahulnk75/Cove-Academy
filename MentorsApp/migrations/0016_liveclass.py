# Generated by Django 5.1.2 on 2025-01-26 11:54

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MentorsApp', '0015_delete_liveclass'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('subject_name', models.CharField(blank=True, max_length=200, null=True)),
                ('topic_name', models.CharField(max_length=200)),
                ('live_start_time', models.DateTimeField()),
                ('zoom_meeting_link', models.URLField(blank=True, null=True)),
                ('zoom_start_url', models.URLField(blank=True, null=True)),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
