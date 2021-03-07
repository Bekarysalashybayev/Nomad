# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app.views import *

urlpatterns = [

    # The home page
    path('', index, name='home'),
    path('/news', news, name='admin-news'),

    # Matches any html file

]
