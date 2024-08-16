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
            resume = form.save(commit=False)
            resume.user = req.user
            resume.save()

            messages.success(req, "新增成功")
            return redirect("resumes:index")
        else:
            return render(req, "resumes/new.html", {"form": form})

    resumes = Resume.objects.order_by("-id")
    return render(req, "resumes/index.html", {"resumes": resumes})


def show(req, id):
    if req.method == "POST":
        resume = get_object_or_404(Resume, pk=id, user=req.user)
        form = ResumeForm(req.POST, instance=resume)

        if form.is_valid():
            form.save()
            messages.success(req, "更新成功")
            return redirect("resumes:show", resume.id)
        else:
            return render(
                req,
                "resumes/edit.html",
                {
                    "form": form,
                    "resume": resume,
                    "bookmarked": resume.bookmarked_by(req.user),
                },
            )

    resume = get_object_or_404(Resume, pk=id)
    comments = resume.comment_set.order_by("-id")

    return render(
        req,
        "resumes/show.html",
        {
            "resume": resume,
            "comments": comments,
            "bookmarked": resume.bookmarked_by(req.user),
        },
    )


@login_required
def new(req):
    form = ResumeForm()
    return render(req, "resumes/new.html", {"form": form})


@login_required
def edit(req, id):
    resume = get_object_or_404(Resume, pk=id, user=req.user)
    form = ResumeForm(instance=resume)
    return render(
        req,
        "resumes/edit.html",
        {"form": form, "resume": resume},
    )


@login_required
def comment(req, id):
    if req.method == "POST":
        resume = get_object_or_404(Resume, pk=id)
        comment = resume.comment_set.create(
            content=req.POST["content"],
            user=req.user,
        )
        return render(
            req,
            "resumes/_comment.html",
            {"comment": comment},
        )


@login_required
def delete_comment(req, id):
    if req.method == "DELETE":
        comment = get_object_or_404(Comment, id=id, user=req.user)
        comment.delete()
        return HttpResponse("")


@login_required
def bookmark(req, id):
    if req.method == "POST":
        resume = get_object_or_404(Resume, pk=id)

        if resume.bookmarked_by(req.user):
            resume.bookmark.remove(req.user)
            return render(
                req,
                "resumes/_bookmark.html",
                {
                    "resume": resume,
                    "bookmarked": False,
                },
            )
        else:
            resume.bookmark.add(req.user)
            return render(
                req,
                "resumes/_bookmark.html",
                {
                    "resume": resume,
                    "bookmarked": True,
                },
            )
