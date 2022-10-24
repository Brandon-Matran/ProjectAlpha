from django.shortcuts import render
from .models import Project

# Create your views here.


def project_list(request):
    project = Project.objects.all()
    context = {
        "project_object": project,
    }
    return render(request, "projects/list.html", context)
