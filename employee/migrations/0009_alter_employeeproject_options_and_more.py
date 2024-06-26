# Generated by Django 5.0.3 on 2024-03-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeeproject',
            options={'ordering': ('priority',), 'verbose_name': 'Employee Project', 'verbose_name_plural': 'Employee Projects'},
        ),
        migrations.RemoveField(
            model_name='employeeproject',
            name='Priority',
        ),
        migrations.RemoveField(
            model_name='employeeproject',
            name='status',
        ),
        migrations.AlterField(
            model_name='employee',
            name='project_status',
            field=models.CharField(blank=True, choices=[('web_development', 'Web Development'), ('devops_engineer', 'Devops Engineer'), ('mobile_app_development', 'Mobile App Development'), ('ui_ux_designing', 'UX / UI Designing')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('high', 'High'), ('low', 'Low'), ('normal', 'Normal'), ('urgent', 'Urgent')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='project_status',
            field=models.CharField(blank=True, choices=[('paused', 'Paused'), ('to_do', 'To do'), ('on_progress', 'On progress'), ('completed', 'Completed')], null=True),
        ),
    ]
