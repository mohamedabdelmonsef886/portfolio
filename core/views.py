from django.shortcuts import render, redirect
from .models import ContactMessage, Project 
# Create your views here.
from .models import ContactMessage

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect("home")
    projects = Project.objects.all() 
    return render(request, "index.html", {"projects": projects})

