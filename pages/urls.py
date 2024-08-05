from .views import about, home
from django.urls import path

urlpatterns = [
    path("", home),
    path("about", about),
]
