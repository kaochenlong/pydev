from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Resume
from .forms import ResumeForm


def index(req):
    if req.method == "POST":
        form = ResumeForm(req.POST)

        if form.is_valid():
            form.save()
            messages.success(req, "新增成功")
            return redirect("resumes:index")
        else:
            return render(req, "resumes/new.html", {"form": form})

    resumes = Resume.objects.all()
    return render(req, "resumes/index.html", {"resumes": resumes})


def show(req, id):
    resume = get_object_or_404(Resume, pk=id)

    if req.method == "POST":
        form = ResumeForm(req.POST, instance=resume)

        if form.is_valid():
            form.save()
            messages.success(req, "更新成功")
            return redirect("resumes:show", resume.id)
        else:
            return render(
                req,
                "resumes/edit.html",
                {"form": form, "resume": resume},
            )

    return render(req, "resumes/show.html", {"resume": resume})


def new(req):
    form = ResumeForm()
    return render(req, "resumes/new.html", {"form": form})


def edit(req, id):
    resume = get_object_or_404(Resume, pk=id)
    form = ResumeForm(instance=resume)
    return render(
        req,
        "resumes/edit.html",
        {"form": form, "resume": resume},
    )
