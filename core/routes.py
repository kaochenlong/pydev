from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("developers/", include("resumes.urls")),
    path("users/", include("users.urls")),
    path("payments/", include("payments.urls")),
    path("", include("pages.urls")),
    path("admin/", admin.site.urls),
] + debug_toolbar_urls()
