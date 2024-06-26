# Generated by Django 5.0.3 on 2024-03-19 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_alter_employee_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, choices=[('web_development', 'Web Development'), ('devops_engineer', 'Devops Engineer'), ('ui_ux_designing', 'UX / UI Designing'), ('mobile_app_development', 'Mobile App Development')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('low', 'Low'), ('normal', 'Normal'), ('high', 'High'), ('urgent', 'Urgent')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='project_status',
            field=models.CharField(blank=True, choices=[('paused', 'Paused'), ('on_progress', 'On progress'), ('to_do', 'To do'), ('completed', 'Completed')], null=True),
        ),
    ]
