from django.urls import path
from . import views
# paths that trigger functions in views file
urlpatterns = [
    path('', views.blank, name='blank'),
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
    path('about', views.about, name='about'),
]

