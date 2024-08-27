from django.urls import path

from . import views

app_name = "resumes"

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("<int:id>", views.show, name="show"),
    path("<int:id>/edit", views.edit, name="edit"),
    path("<int:id>/bookmark", views.bookmark, name="bookmark"),
    path("<int:id>/comments", views.comment, name="comment"),
    path("comments/<int:id>", views.delete_comment, name="delete_comment"),
]
