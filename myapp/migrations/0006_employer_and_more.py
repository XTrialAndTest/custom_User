# Generated by Django 4.2.1 on 2023-06-01 12:55

import cloudinary.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_applicantprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('myapp.customuser',),
            managers=[
                ('applicant', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='applicantprofile',
            old_name='profile_Pic',
            new_name='profile_pic',
        ),
        migrations.CreateModel(
            name='EmployerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=500)),
                ('logo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_pic')),
                ('contact', models.CharField(max_length=12)),
                ('hq', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]