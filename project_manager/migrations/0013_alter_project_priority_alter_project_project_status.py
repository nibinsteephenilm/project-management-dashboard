# Generated by Django 5.0.3 on 2024-03-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0012_project_employee_projectmanger_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(blank=True, choices=[('high', 'High'), ('low', 'Low'), ('normal', 'Normal'), ('urgent', 'Urgent')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('paused', 'Paused'), ('to_do', 'To do'), ('on_progress', 'On progress'), ('completed', 'Completed')], max_length=50, null=True),
        ),
    ]
