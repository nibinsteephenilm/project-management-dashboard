# Generated by Django 5.0.3 on 2024-03-19 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_remove_employee_employee_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, choices=[('web_development', 'Web Development'), ('mobile_app_development', 'Mobile App Development'), ('devops_engineer', 'Devops Engineer'), ('ui_ux_designing', 'UX / UI Designing')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('high', 'High'), ('urgent', 'Urgent'), ('normal', 'Normal'), ('low', 'Low')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='project_status',
            field=models.CharField(blank=True, choices=[('to_do', 'To do'), ('paused', 'Paused'), ('on_progress', 'On progress'), ('completed', 'Completed')], null=True),
        ),
    ]
