# Generated by Django 4.1.7 on 2023-03-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0016_alter_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='external_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
