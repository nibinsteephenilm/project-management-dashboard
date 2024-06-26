from django.shortcuts import render,redirect
from project_manager.models import Project,ProjectManager
from employee.models import EmployeeProject,Employee
from django.http import HttpResponse,JsonResponse
from datetime import date,datetime


def index(request):
    return render(request,'base.html')


def dashboard(request):

    projects = Project.objects.all()
    employees = Employee.objects.all()

    current_user = request.user
    employee_model = Employee.objects.all()
    all_projects_count = Project.objects.filter(project_manager__user=current_user).count()
    completed_projects_count = Project.objects.filter(project_manager__user=current_user, project_status="completed").count()
    ongoing_projects_count = Project.objects.filter(project_manager__user=current_user, project_status="on_progress").count()
    overdue_projects_count = Project.objects.filter(project_manager__user=current_user, project_status="over_due").count()

    today_deadline_projects = Project.objects.filter(project_manager__user=current_user, submission_date__date=datetime.today())
    today_assigned_projects = EmployeeProject.objects.filter(assign_date__date=date.today())
    overdue_projects = Project.objects.filter(project_manager__user=current_user,submission_date__date__lt=datetime.today())

    context = {
        'all_projects_count' : all_projects_count,
        'completed_projects_count' : completed_projects_count,
        'ongoing_projects_count' : ongoing_projects_count,
        'overdue_projects_count' : overdue_projects_count,
        'today_deadline_projects' : today_deadline_projects,
        'today_assigned_projects' : today_assigned_projects,
        'overdue_projects': overdue_projects,
        'current_user' : current_user,
        'employees' : employees,
        'projects' : projects
    }

    return render(request,'dashboard.html',context)


def project(request):
    current_user = request.user
    project_status = request.GET.get('status')
    projects = Project.objects.all()
    employees = Employee.objects.all()

    if project_status == 'all':
        all_projects = EmployeeProject.objects.filter(project__project_manager__user=current_user)
    elif project_status == 'completed':
        all_projects = EmployeeProject.objects.filter(project__project_manager__user=current_user, project_status="completed")
    elif project_status == 'in-progress':
        all_projects = EmployeeProject.objects.filter(project__project_manager__user=current_user, project_status="on_progress")
    elif project_status == 'overdue':
        all_projects = EmployeeProject.objects.filter(project__project_manager__user=current_user, project_status="over_due")

    context = {
        'current_user': current_user,
        'all_projects': all_projects,
        'employees' : employees,
        'projects' : projects
    }

    return render(request,'project.html',context)

def single(request,project_id):
    current_user = request.user
    projects = Project.objects.all()
    employees = Employee.objects.all()

    try:
        singleProject = EmployeeProject.objects.get(pk=project_id)
        if singleProject.employee.designation == 'mobile_app_development' or 'web_development':
            team = 'Development'
        elif singleProject.employee.designation == 'ui_ux_designing':
            team = 'Designing'
        elif singleProject.employee.designation == 'devops_engineer':
            team = 'Devops'
        else: 
            team == 'No team assigned'
        
    except Project.DoesNotExist:
        return render(request,'emptyProject.html')

    context = {
        'singleProject' : singleProject,
        'team' : team,
        'current_user' : current_user,
        'employees' : employees,
        'projects' : projects
    }
    
    return render(request,'projectSingle.html',context)

def employee_project_info(request,employee_project_id):

    if EmployeeProject.objects.filter(pk=employee_project_id).exists():
        project = EmployeeProject.objects.filter(pk=employee_project_id).first()
        
        data = {
            "description":project.description,
            "updated_by":project.project.project_manager.name,
            "current_status":project.project_status,
            "updated_on":project.date_added,
        }

        print(data)

    return JsonResponse(data)

def empty(request):
    return render(request,'emptyProject.html')


def edit(request, id):

    project_id = request.POST.get('project_name')
    description = request.POST.get('description')
    task_priority = request.POST.get('task_priority')
    assign_date = request.POST.get('assign_date')
    due_date = request.POST.get('assign_date')
    assigned_to_id = request.POST.get('assigned_to')

    project = Project.objects.get(id=project_id)
    assigned_to = Employee.objects.get(id=assigned_to_id)
    employee_project = EmployeeProject.objects.get(id=id)

    employee_project.project = project
    employee_project.project.description = description
    employee_project.assign_date = assign_date
    employee_project.due_date = due_date
    employee_project.priority = task_priority
    employee_project.employee = assigned_to

    employee_project.project.team_lead.save()
    employee_project.employee.save()
    employee_project.project.save()
    employee_project.save()


    return redirect('single', project_id=employee_project.id)


def create(request):
    current_user = request.user
    project_name = request.POST.get('project_name')
    description = request.POST.get('description')
    priority = request.POST.get('project_priority')
    team_lead_id = request.POST.get('team_lead')
    client_name = request.POST.get('client_name')
    client_email = request.POST.get('client_email')
    team_lead = Employee.objects.get(id=team_lead_id)
    start_date = request.POST.get('start_date')
    submission_date = request.POST.get('submission_date')
    project_manager= ProjectManager.objects.get(user=current_user)
     
    new_project = Project.objects.create(
        name=project_name,
        description=description,
        priority=priority,
        team_lead=team_lead,
        client_name=client_name,
        client_email=client_email,
        project_manager=project_manager,
        start_date=start_date,
        submission_date=submission_date
    )
        
    return redirect('dashboard') 

def task(request):
    project_id = request.POST.get('project_name')
    description = request.POST.get('description')
    task_priority = request.POST.get('task_priority')
    assign_date = request.POST.get('assign_date')
    due_date = request.POST.get('assign_date')
    assigned_to_id = request.POST.get('assigned_to')

    project = Project.objects.get(id=project_id)
    assigned_to = Employee.objects.get(id=assigned_to_id)
    

    new_employee_project = EmployeeProject.objects.create(
        project = project,
        description = description,
        priority = task_priority,
        assign_date = assign_date,
        due_date = due_date,
        employee = assigned_to
    )

    return redirect('dashboard')

def cancelCreate(request):
    return redirect('dashboard')
def cancelTask(request):
    return redirect('project')
