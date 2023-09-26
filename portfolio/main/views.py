from django.shortcuts import render
from .models import About


def home(request):
    about = About.objects.first()
    print(about.socials.all())
    return render(request, "main/home.html", {"about": about})
