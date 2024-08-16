from django.urls import path

from resumes import views as resume_views

from . import views

app_name = "pages"

urlpatterns = [
    path("", resume_views.index, name="root"),
    path("about", views.about, name="about"),
]
