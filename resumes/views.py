from django.shortcuts import render, get_object_or_404, redirect
from .models import Resume
from django.http import HttpResponse
from .forms import ResumeForm


def index(req):
    if req.method == "POST":
        form = ResumeForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect("resumes:index")
        else:
            return HttpResponse("bad!!")

    resumes = Resume.objects.all()
    return render(req, "resumes/index.html", {"resumes": resumes})


def show(req, id):
    resume = get_object_or_404(Resume, pk=id)
    return HttpResponse(resume.email)


def new(req):
    form = ResumeForm()
    return render(req, "resumes/new.html", {"form": form})
