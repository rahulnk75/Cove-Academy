# Generated by Django 5.1.2 on 2024-12-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meander_Register_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=200, null=True)),
                ('Qualification', models.CharField(blank=True, max_length=200, null=True)),
                ('Experience', models.CharField(blank=True, max_length=200, null=True)),
                ('Password', models.CharField(blank=True, max_length=200, null=True)),
                ('C_password', models.CharField(blank=True, max_length=200, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question_Paper_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Date', models.CharField(blank=True, max_length=200, null=True)),
                ('Q_PDF_file', models.FileField(blank=True, null=True, upload_to='Study_material_Pdfs')),
                ('Description', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Study_Material_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_name', models.CharField(blank=True, max_length=200, null=True)),
                ('Topic', models.CharField(blank=True, max_length=200, null=True)),
                ('S_PDF_file', models.FileField(blank=True, null=True, upload_to='Study_material_Pdfs')),
                ('Description', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextBook_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_name', models.CharField(blank=True, max_length=200, null=True)),
                ('Scert_Ncert', models.CharField(blank=True, max_length=200, null=True)),
                ('Class', models.CharField(blank=True, max_length=200, null=True)),
                ('PDF_file', models.FileField(blank=True, null=True, upload_to='Textbook_Pdfs')),
                ('Textbook_Images', models.ImageField(blank=True, null=True, upload_to='Textbook_Images')),
                ('Description', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
