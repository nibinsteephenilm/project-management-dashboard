# Generated by Django 5.0.3 on 2024-03-16 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contact_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
