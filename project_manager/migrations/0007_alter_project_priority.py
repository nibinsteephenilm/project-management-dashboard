# Generated by Django 5.0.3 on 2024-03-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0006_project_priority_project_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Prgent', 'High'), ('High', 'Low')], max_length=50, null=True),
        ),
    ]
