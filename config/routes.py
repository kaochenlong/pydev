from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("developers/", include("apps.resumes.urls")),
    path("users/", include("apps.users.urls")),
    path("payments/", include("apps.payments.urls")),
    path("", include("apps.pages.urls")),
    path("admin/", admin.site.urls),
] + debug_toolbar_urls()
