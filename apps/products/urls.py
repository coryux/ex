from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('/', views.products),
    path('/<number>/', views.product),
    #path('<slug>/',views.article_details),
]
