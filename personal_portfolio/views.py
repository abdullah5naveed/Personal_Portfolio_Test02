from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all()
    homeData = {'projects':projects}
    return render(request, 'personal_portfolio/home.html', homeData)

