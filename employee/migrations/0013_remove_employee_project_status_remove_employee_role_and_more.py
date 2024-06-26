# Generated by Django 5.0.3 on 2024-03-18 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_employee_employee_project_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='project_status',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='role',
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, choices=[('devops_engineer', 'Devops Engineer'), ('mobile_app_development', 'Mobile App Development'), ('web_development', 'Web Development'), ('ui_ux_designing', 'UX / UI Designing')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('low', 'Low'), ('urgent', 'Urgent'), ('high', 'High'), ('normal', 'Normal')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='project_status',
            field=models.CharField(blank=True, choices=[('completed', 'Completed'), ('on_progress', 'On progress'), ('paused', 'Paused'), ('to_do', 'To do')], null=True),
        ),
    ]
