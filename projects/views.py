from django.shortcuts import render, get_object_or_404
from .models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def project_list(request):
    project = Project.objects.filter(owner=request.user)
    context = {
        "project_object": project,
    }
    return render(request, "projects/list.html", context)

@login_required
def show_project(request, id):
    details = get_object_or_404(Project, id=id)
    context = {
        "detail_object": details,
    }
    return render(request, "projects/details.html", context)
