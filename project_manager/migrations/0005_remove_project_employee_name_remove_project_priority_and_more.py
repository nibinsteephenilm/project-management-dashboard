# Generated by Django 5.0.3 on 2024-03-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0004_projectmanger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='employee_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('name',), 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='projectmanger',
            options={'ordering': ('name',), 'verbose_name': 'project manager', 'verbose_name_plural': 'project managers'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='client_mail',
            new_name='client_email',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='projectmanger',
            old_name='pm_id',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='projectmanger',
            old_name='pm_name',
            new_name='userid',
        ),
        migrations.RemoveField(
            model_name='project',
            name='assigned_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='project',
            name='team',
        ),
        migrations.RemoveField(
            model_name='project',
            name='team_lead',
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='submission_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Priority',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
