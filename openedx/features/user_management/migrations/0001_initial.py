# Generated by Django 3.2.17 on 2023-03-22 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0003_historicalorganizationcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=100)),
                ('batch_description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=1)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('last_modified_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userbatch_organization', to='organizations.organization')),
            ],
            options={
                'verbose_name': 'User Batches',
                'db_table': 'usermanagement_userbatches',
            },
        ),
        migrations.CreateModel(
            name='UserBatchMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userbatchmapping_user', to=settings.AUTH_USER_MODEL)),
                ('user_batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userbatchmapping_userbatch', to='user_management.userbatch')),
            ],
            options={
                'verbose_name': 'User Batch Mapping',
                'db_table': 'usermanagement_userbatchmapping',
            },
        ),
    ]