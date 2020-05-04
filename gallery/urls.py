# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('art/', views.art, name='gallery-art'),
    path('writing/', views.writing, name='gallery-writing'),
    path('code/', views.code, name='gallery-code'),
    path('<int:year>/<int:month>/<int:day>/<str:title>', views.view, name='gallery-view')
]
