from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_text, name='create_tex'),
    path('<slug:slug>/', views.view_text, name='view_text'),
    path('<slug:slug>/edit', views.edit_text, name='edit_text'),
]