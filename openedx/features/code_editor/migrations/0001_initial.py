# Generated by Django 3.2.17 on 2023-03-22 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edx_proctoring', '0024_delete_proctoredexamstudentattempthistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_id', models.CharField(max_length=200)),
                ('question_id', models.CharField(max_length=200)),
                ('coding_Languages_type', models.CharField(choices=[('BACKEND', 'BACKEND'), ('DATABASE', 'DATABASE'), ('DEVOPS', 'DEVOPS'), ('FRONTEND', 'FRONTEND')], max_length=50)),
                ('coding_Languages', models.CharField(blank=True, default='', max_length=200)),
                ('enable_code_run', models.BooleanField(default=True)),
                ('enable_copy_paste', models.BooleanField(default=False)),
                ('evaluvation_parameters', models.TextField(blank=True, null=True)),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('max_score', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('auto_evaluation', models.BooleanField(default=True)),
                ('default_snippet_id', models.CharField(blank=True, max_length=500, null=True)),
                ('result_snippet_id', models.CharField(blank=True, max_length=500, null=True)),
                ('allow_main_method', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('proctored_exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='codingexam_exam', to='edx_proctoring.proctoredexam')),
            ],
            options={
                'verbose_name': 'Coding Question',
                'db_table': 'coding_questions',
            },
        ),
        migrations.CreateModel(
            name='DefaultSnippet',
            fields=[
                ('snippet_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('snippet_name', models.CharField(max_length=200)),
                ('snippet_text', models.TextField(null=True)),
                ('coding_language', models.CharField(max_length=200)),
                ('coding_Languages_type', models.CharField(choices=[('BACKEND', 'BACKEND'), ('DATABASE', 'DATABASE'), ('DEVOPS', 'DEVOPS'), ('FRONTEND', 'FRONTEND')], max_length=50)),
            ],
            options={
                'verbose_name': 'Default Snippet',
                'db_table': 'default_snippets',
            },
        ),
        migrations.CreateModel(
            name='CodingResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.CharField(max_length=200)),
                ('unit_id', models.CharField(max_length=200)),
                ('snippet_id', models.CharField(max_length=50)),
                ('snippet_url', models.CharField(max_length=100)),
                ('snippet_text', models.TextField(null=True)),
                ('snippet_language', models.CharField(max_length=100)),
                ('score', models.CharField(blank=True, max_length=100, null=True)),
                ('result', models.CharField(blank=True, max_length=100, null=True)),
                ('grade', models.CharField(blank=True, max_length=100, null=True)),
                ('is_graded', models.BooleanField(default=False)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('evaluation_details', models.TextField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('is_submit', models.BooleanField(default=False)),
                ('coding_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coding_attempt_exam', to='code_editor.codingquestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coding_attempt_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Coding Attempt',
                'db_table': 'coding_studentattempt',
            },
        ),
    ]
