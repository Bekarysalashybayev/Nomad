# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path("admin-panel/", include("authentication.urls")),  # Auth routes - login / register
    path("admin-panel/", include("app.urls")),
    path("", include("mainsite.urls"))
]