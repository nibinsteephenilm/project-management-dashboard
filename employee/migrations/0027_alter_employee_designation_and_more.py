# Generated by Django 5.0.3 on 2024-03-20 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0026_alter_employee_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, choices=[('ui_ux_designing', 'UX / UI Designing'), ('devops_engineer', 'Devops Engineer'), ('web_development', 'Web Development'), ('mobile_app_development', 'Mobile App Development')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('normal', 'Normal'), ('high', 'High'), ('low', 'Low'), ('urgent', 'Urgent')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='project_status',
            field=models.CharField(blank=True, choices=[('completed', 'Completed'), ('paused', 'Paused'), ('on_progress', 'On progress'), ('to_do', 'To do')], null=True),
        ),
    ]
