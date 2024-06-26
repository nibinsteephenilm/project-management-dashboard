# Generated by Django 5.0.3 on 2024-03-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0002_project_contact_number_project_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='client_contact_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='client_mail',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='client_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
