# Generated by Django 5.1.2 on 2024-11-04 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam_db',
            old_name='Exam_Name',
            new_name='Exam_Category',
        ),
    ]