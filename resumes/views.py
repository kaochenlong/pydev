from django.shortcuts import render, get_object_or_404
from .models import Resume
from django.http import HttpResponse


def index(req):
    resumes = Resume.objects.all()
    return render(req, "resumes/index.html", {"resumes": resumes})


def show(req, id):
    resume = get_object_or_404(Resume, pk=id)
    return HttpResponse(resume.email)
