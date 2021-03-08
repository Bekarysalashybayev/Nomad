# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app.views import *

urlpatterns = [

    # The home page
    path('', index, name='home'),
    path('profile', profile, name='profile'),
    path('news', news, name='admin-news'),
    path('add-news', add_news, name='admin-add-news'),
    path('news/update/<int:news_id>', update_news),
    path('news/delete/<int:news_id>', delete_news),
    path('contacts', contactforms, name='contactforms'),
    path('contact/delete/<int:contact_id>', delete_contact_form, ),

    # Matches any html file

]
