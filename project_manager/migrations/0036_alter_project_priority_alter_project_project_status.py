# Generated by Django 5.0.3 on 2024-03-21 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0035_alter_project_priority_alter_project_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(blank=True, choices=[('normal', 'Normal'), ('urgent', 'Urgent'), ('low', 'Low'), ('high', 'High')], null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('completed', 'Completed'), ('paused', 'Paused'), ('over_due', 'Overdue'), ('on_progress', 'On progress'), ('to_do', 'To do')], null=True),
        ),
    ]
