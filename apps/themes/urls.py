from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('/', views.themes),
    path('/<number>/', views.theme),
    #path('<slug>/',views.article_details),
]

#urlpatterns += staticfiles_urlpatterns()
