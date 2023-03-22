# Generated by Django 3.2.17 on 2023-03-20 08:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import opaque_keys.edx.django.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0044_courseenrollmentcelebration_celebrate_weekly_goal'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'auth_Allow_Registration_Page',
                'permissions': (('can_deactivate_users', 'Can deactivate, but NOT delete users'),),
            },
        ),
        migrations.CreateModel(
            name='CourseIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AssessmentIdentifier', models.CharField(db_index=True, max_length=60)),
                ('CourseKey', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'auth_CourseIdentifiers',
                'permissions': (('can_deactivate_users', 'Can deactivate, but NOT delete users'),),
            },
        ),
        migrations.CreateModel(
            name='UserCourseAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', opaque_keys.edx.django.models.CourseKeyField(db_index=True, max_length=255)),
                ('active_status', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'auth_usecourse_access',
                'permissions': (('can_deactivate_users', 'Can deactivate, but NOT delete users'),),
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='allow_assessment',
            field=models.BooleanField(default=0),
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(db_index=True, max_length=255)),
                ('middleName', models.CharField(blank=True, max_length=255)),
                ('lastName', models.CharField(blank=True, max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('dateOfBirth', models.DateField()),
                ('contactNumber', models.CharField(max_length=12)),
                ('emailId', models.EmailField(max_length=254)),
                ('identyType', models.CharField(max_length=255)),
                ('identyNo', models.CharField(max_length=255)),
                ('percentage10', models.CharField(max_length=5)),
                ('percentage12', models.CharField(max_length=5)),
                ('qualification', models.CharField(max_length=100)),
                ('stream', models.CharField(max_length=100)),
                ('collageName', models.CharField(max_length=100)),
                ('yearOfPassing', models.IntegerField()),
                ('gradPercentage', models.CharField(max_length=100)),
                ('postGradPercentage', models.CharField(max_length=100)),
                ('drive', models.CharField(max_length=50)),
                ('informationSource', models.CharField(max_length=50)),
                ('backlogs', models.CharField(max_length=10)),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 33, 29, 986326, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userregistration', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_userregistration',
                'permissions': (('can_deactivate_users', 'Can deactivate, but NOT delete users'),),
            },
        ),
    ]