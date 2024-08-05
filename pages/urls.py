from .views import about, home
from django.urls import path

app_name = "pages"

urlpatterns = [
    path("", home, name="root"),
    path("about", about, name="about"),
]
