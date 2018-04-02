from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.epics),
    path('/<number>/', views.epic),
]

#urlpatterns += staticfiles_urlpatterns()
