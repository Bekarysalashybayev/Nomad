# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.conf.urls.static import static
from core import settings
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path("admin-panel/", include("authentication.urls")),  # Auth routes - login / register
    path("admin-panel/", include("app.urls")),
    path("", include("mainsite.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
