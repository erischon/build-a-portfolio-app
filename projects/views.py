from django.shortcuts import render
from projects.models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})
