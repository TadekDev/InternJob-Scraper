# Generated by Django 4.1.7 on 2023-05-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0033_country_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_opportunity_emails_job_last_run', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
