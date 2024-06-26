from django.contrib import admin
from project_manager.models import Project,ProjectManager

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'submission_date', 'priority', 'project_status', 'team_lead', 'client_name', 'client_email', 'project_manager')

@admin.register(ProjectManager)
class ProjectManagerAdmin(admin.ModelAdmin):
    list_display = ('name','userid','password','mobile_number', 'user')