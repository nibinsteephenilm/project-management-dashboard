# Generated by Django 5.0.3 on 2024-03-16 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=256)),
                ('Priority', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Employee Project',
                'verbose_name_plural': 'Employee Projectss',
                'db_table': 'employee_employee_project',
                'ordering': ('status',),
            },
        ),
    ]
