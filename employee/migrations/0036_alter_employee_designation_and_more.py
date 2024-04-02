# Generated by Django 5.0.3 on 2024-03-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0035_alter_employee_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, choices=[('devops_engineer', 'Devops Engineer'), ('mobile_app_development', 'Mobile App Development'), ('web_development', 'Web Development'), ('ui_ux_designing', 'UX / UI Designing')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('urgent', 'Urgent'), ('normal', 'Normal'), ('high', 'High'), ('low', 'Low')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='project_status',
            field=models.CharField(blank=True, choices=[('to_do', 'To do'), ('over_due', 'Overdue'), ('paused', 'Paused'), ('completed', 'Completed'), ('on_progress', 'On progress')], null=True),
        ),
    ]