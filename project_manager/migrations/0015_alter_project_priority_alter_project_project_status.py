# Generated by Django 5.0.3 on 2024-03-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0014_alter_project_priority_alter_project_project_status'),
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
            field=models.CharField(blank=True, choices=[('on_progress', 'On progress'), ('paused', 'Paused'), ('completed', 'Completed'), ('to_do', 'To do')], null=True),
        ),
    ]
