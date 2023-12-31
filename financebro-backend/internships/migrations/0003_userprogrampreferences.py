# Generated by Django 4.1.7 on 2023-03-03 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('internships', '0002_alter_userprogram_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProgramPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regions', models.JSONField(default=[])),
                ('company_categories', models.JSONField(default=[])),
                ('program_categories', models.JSONField(default=[])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Preferences',
                'verbose_name_plural': 'User(s) Preferences',
            },
        ),
    ]
