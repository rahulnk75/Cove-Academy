# Generated by Django 5.1.2 on 2024-11-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_rename_exam_name_exam_db_exam_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam_Categories', models.CharField(blank=True, max_length=200, null=True)),
                ('Exam_Name', models.TextField(blank=True, max_length=200, null=True)),
                ('Category_Images', models.ImageField(blank=True, null=True, upload_to='Course_Images')),
                ('Course_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Course_fees', models.IntegerField(blank=True, null=True)),
                ('Course_Images', models.ImageField(blank=True, null=True, upload_to='Course_Images')),
                ('Start_Date', models.DateField(blank=True, null=True)),
                ('End_date', models.DateField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]