# Generated by Django 5.0.3 on 2024-03-19 04:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_employeeproject_project_alter_employee_designation_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user_id',
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, choices=[('devops_engineer', 'Devops Engineer'), ('mobile_app_development', 'Mobile App Development'), ('ui_ux_designing', 'UX / UI Designing'), ('web_development', 'Web Development')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('high', 'High'), ('low', 'Low'), ('normal', 'Normal'), ('urgent', 'Urgent')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='project_status',
            field=models.CharField(blank=True, choices=[('on_progress', 'On progress'), ('completed', 'Completed'), ('paused', 'Paused'), ('to_do', 'To do')], null=True),
        ),
    ]
