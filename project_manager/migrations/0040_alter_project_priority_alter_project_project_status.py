# Generated by Django 5.0.3 on 2024-03-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0039_alter_project_priority_alter_project_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(blank=True, choices=[('urgent', 'Urgent'), ('normal', 'Normal'), ('high', 'High'), ('low', 'Low')], null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('to_do', 'To do'), ('over_due', 'Overdue'), ('paused', 'Paused'), ('completed', 'Completed'), ('on_progress', 'On progress')], null=True),
        ),
    ]
