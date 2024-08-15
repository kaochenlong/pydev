from django.urls import path

from .views import about, home

app_name = "pages"

urlpatterns = [
    path("", home, name="root"),
    path("about", about, name="about"),
]
