from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.stories),
    path('/<number>/', views.story),
]


#urlpatterns += staticfiles_urlpatterns()
