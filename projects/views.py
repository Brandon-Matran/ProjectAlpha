from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from projects.forms import ProjectForm
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


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
        return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create.html", context)
