# Generated by Django 5.0.3 on 2024-03-18 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_alter_employee_options_and_more'),
        ('project_manager', '0011_alter_project_priority_alter_project_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='employee',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AddField(
            model_name='projectmanger',
            name='project',
            field=models.ManyToManyField(blank=True, null=True, to='project_manager.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(blank=True, choices=[('urgent', 'Urgent'), ('low', 'Low'), ('high', 'High'), ('normal', 'Normal')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('on_progress', 'On progress'), ('completed', 'Completed'), ('paused', 'Paused'), ('to_do', 'To do')], max_length=50, null=True),
        ),
    ]
