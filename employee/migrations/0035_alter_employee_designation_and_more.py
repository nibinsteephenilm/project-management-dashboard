# Generated by Django 5.0.3 on 2024-03-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0034_employeeproject_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, choices=[('ui_ux_designing', 'UX / UI Designing'), ('web_development', 'Web Development'), ('mobile_app_development', 'Mobile App Development'), ('devops_engineer', 'Devops Engineer')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('high', 'High'), ('normal', 'Normal'), ('low', 'Low'), ('urgent', 'Urgent')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='project_status',
            field=models.CharField(blank=True, choices=[('over_due', 'Overdue'), ('to_do', 'To do'), ('on_progress', 'On progress'), ('completed', 'Completed'), ('paused', 'Paused')], null=True),
        ),
    ]
