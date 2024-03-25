# Generated by Django 5.0.3 on 2024-03-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0003_project_client_contact_number_project_client_mail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectManger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm_name', models.CharField(max_length=156)),
                ('pm_id', models.CharField(max_length=156)),
                ('password', models.CharField(max_length=156)),
                ('mobile_number', models.CharField(max_length=156)),
            ],
            options={
                'verbose_name': 'project manager',
                'verbose_name_plural': 'project managers',
                'db_table': 'project_manager_project_manger',
                'ordering': ('pm_name',),
            },
        ),
    ]
