# Generated by Django 4.1.7 on 2023-04-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0025_delete_jpmorganprogramsummary'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='countries_mapped',
            field=models.ManyToManyField(to='internships.country'),
        ),
    ]
