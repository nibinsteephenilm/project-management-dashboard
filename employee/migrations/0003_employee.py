# Generated by Django 5.0.3 on 2024-03-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employeeproject_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=256)),
                ('role', models.CharField(max_length=256)),
                ('mobile_no', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=110)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'employee_employee',
                'ordering': ('employee_name',),
            },
        ),
    ]
