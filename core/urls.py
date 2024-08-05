from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("developers/", include("resumes.urls")),
    path("", include("pages.urls")),
    path("admin/", admin.site.urls),
]
