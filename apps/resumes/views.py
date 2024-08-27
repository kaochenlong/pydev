import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ResumeForm
from .models import Comment, Resume


def index(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)

        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            messages.success(request, "新增成功")
            return redirect("resumes:index")
        else:
            return render(request, "resumes/new.html", {"form": form})

    resumes = Resume.objects.prefetch_related("user", "tags").order_by("-id")

    keyword = request.GET.get("keyword", "")
    if keyword:
        resumes = resumes.filter(
            Q(profile__contains=keyword)
            | Q(introduce__contains=keyword)
            | Q(user__username__contains=keyword)
        )

    return render(
        request,
        "resumes/index.html",
        {
            "resumes": resumes,
            "keyword": keyword,
        },
    )


def show(request, id):
    if request.method == "POST":
        resume = get_object_or_404(Resume, pk=id, user=request.user)
        form = ResumeForm(request.POST, instance=resume)

        if form.is_valid():
            obj = form.save(commit=False)

            tags = request.POST.get("tags")
            if tags:
                tags = [tag["value"] for tag in json.loads(tags)]
                obj.tags.set(tags)

            form.save_m2m()

            messages.success(request, "更新成功")
            return redirect("resumes:show", resume.id)
        else:
            return render(
                request,
                "resumes/edit.html",
                {
                    "form": form,
                    "resume": resume,
                    "bookmarked": resume.bookmarked_by(request.user),
                },
            )

    resume = get_object_or_404(Resume, pk=id)
    comments = resume.comment_set.prefetch_related("user").order_by("-id")

    return render(
        request,
        "resumes/show.html",
        {
            "resume": resume,
            "comments": comments,
            "bookmarked": resume.bookmarked_by(request.user),
        },
    )


@login_required
def new(request):
    form = ResumeForm()
    return render(request, "resumes/new.html", {"form": form})


@login_required
def edit(request, id):
    resume = get_object_or_404(Resume, pk=id, user=request.user)
    form = ResumeForm(instance=resume)
    return render(
        request,
        "resumes/edit.html",
        {"form": form, "resume": resume},
    )


@login_required
def comment(request, id):
    if request.method == "POST":
        resume = get_object_or_404(Resume, pk=id)
        comment = resume.comment_set.create(
            content=request.POST["content"],
            user=request.user,
        )
        return render(
            request,
            "resumes/_comment.html",
            {"comment": comment},
        )


@login_required
def delete_comment(request, id):
    if request.method == "DELETE":
        comment = get_object_or_404(Comment, id=id, user=request.user)
        comment.delete()
        return HttpResponse("")


@login_required
def bookmark(request, id):
    if request.method == "POST":
        resume = get_object_or_404(Resume, pk=id)

        if resume.bookmarked_by(request.user):
            resume.bookmark.remove(request.user)
            return render(
                request,
                "resumes/_bookmark.html",
                {
                    "resume": resume,
                    "bookmarked": False,
                },
            )
        else:
            resume.bookmark.add(request.user)
            return render(
                request,
                "resumes/_bookmark.html",
                {
                    "resume": resume,
                    "bookmarked": True,
                },
            )
