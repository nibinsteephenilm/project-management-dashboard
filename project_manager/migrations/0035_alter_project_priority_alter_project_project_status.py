# Generated by Django 5.0.3 on 2024-03-21 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0034_alter_project_priority_alter_project_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(blank=True, choices=[('high', 'High'), ('low', 'Low'), ('urgent', 'Urgent'), ('normal', 'Normal')], null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('paused', 'Paused'), ('to_do', 'To do'), ('over_due', 'Overdue'), ('on_progress', 'On progress'), ('completed', 'Completed')], null=True),
        ),
    ]