# Generated by Django 5.0.3 on 2024-03-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_employeeproject_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='project_status',
            field=models.CharField(blank=True, choices=[('Web DEvelopment', 'Devops Engineer'), ('UX / UI Designing', 'Mobile App Development')], max_length=50, null=True),
        ),
    ]
