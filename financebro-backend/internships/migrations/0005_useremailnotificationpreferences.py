# Generated by Django 4.1.7 on 2023-03-03 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('internships', '0004_alter_userprogrampreferences_company_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEmailNotificationPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_notifications_enabled', models.BooleanField(default=True)),
                ('regions', models.JSONField(default=list)),
                ('company_categories', models.JSONField(default=list)),
                ('program_categories', models.JSONField(default=list)),
                ('emails_per_day_count', models.PositiveIntegerField(blank=True, null=True)),
                ('near_deadline_notifications_enabled', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Email Preferences',
                'verbose_name_plural': 'User(s) Email Preferences',
            },
        ),
    ]
