# Generated by Django 5.1.2 on 2024-11-07 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_course_db'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_db',
            name='Category_Images',
        ),
    ]
