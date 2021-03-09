
from django.urls import path, re_path
from mainsite import views


urlpatterns = [
    path('', views.index, name='home'),
    path('/insurance', views.insurance, name='insurance'),
    path('/insurance/add/<int:insurance_id>', views.add_issue, name='add-issue'),
    path('/about', views.about, name='about'),
    path('/resources/<int:insurance_id>', views.resources, name='resources'),
    path('/contact', views.contact, name='contact'),
    path('/news', views.news, name='news'),
    path('/news/detail/<int:news_id>', views.news_detail, name='news-detail'),
]