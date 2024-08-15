from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("developers/", include("resumes.urls")),
    path("users/", include("users.urls")),
    path("", include("pages.urls")),
    path("admin/", admin.site.urls),
]
