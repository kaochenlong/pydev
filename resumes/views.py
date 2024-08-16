from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ResumeForm
from .models import Comment, Resume


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

    comments = resume.comment_set.order_by("-id")

    return render(
        req,
        "resumes/show.html",
        {
            "resume": resume,
            "comments": comments,
        },
    )


@login_required
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


def comment(req, id):
    if req.method == "POST":
        resume = get_object_or_404(Resume, pk=id)
        comment = resume.comment_set.create(content=req.POST["content"])
        return render(
            req,
            "resumes/_comment.html",
            {"comment": comment},
        )


def delete_comment(req, id):
    if req.method == "DELETE":
        comment = get_object_or_404(Comment, id=id)
        comment.delete()
        return HttpResponse("")
