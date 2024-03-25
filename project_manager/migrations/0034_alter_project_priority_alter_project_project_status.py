# Generated by Django 5.0.3 on 2024-03-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0033_alter_project_priority_alter_project_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(blank=True, choices=[('low', 'Low'), ('urgent', 'Urgent'), ('high', 'High'), ('normal', 'Normal')], null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('on_progress', 'On progress'), ('paused', 'Paused'), ('over_due', 'Overdue'), ('to_do', 'To do'), ('completed', 'Completed')], null=True),
        ),
    ]