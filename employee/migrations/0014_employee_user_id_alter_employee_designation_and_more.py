# Generated by Django 5.0.3 on 2024-03-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_remove_employee_project_status_remove_employee_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='user_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, choices=[('ui_ux_designing', 'UX / UI Designing'), ('devops_engineer', 'Devops Engineer'), ('web_development', 'Web Development'), ('mobile_app_development', 'Mobile App Development')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('normal', 'Normal'), ('high', 'High'), ('urgent', 'Urgent'), ('low', 'Low')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='project_status',
            field=models.CharField(blank=True, choices=[('to_do', 'To do'), ('on_progress', 'On progress'), ('completed', 'Completed'), ('paused', 'Paused')], null=True),
        ),
    ]
