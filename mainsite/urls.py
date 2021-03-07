
from django.urls import path, re_path
from mainsite import views


urlpatterns = [
    path('', views.index, name='home'),
    path('/insurance', views.insurance, name='insurance'),
    path('/about', views.about, name='about'),
    path('/resources', views.resources, name='resources'),
    path('/contact', views.contact, name='contact'),
    path('/news', views.news, name='news'),
]