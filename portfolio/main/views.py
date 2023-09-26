from django.shortcuts import render
from .models import About, Project, Skill


def home(request):
    about = About.objects.first()
    projects = Project.objects.all()
    all_skills = Skill.objects.all()
    return render(
        request,
        "main/home.html",
        {
            "about": about,
            "projects": projects,
            "skills": all_skills,
        },
    )
