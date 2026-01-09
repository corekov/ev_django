from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tables/', views.index, name='index'),

    path('counties/', views.county_list, name='county_list'),
    path('counties/add/', views.county_create, name='county_add'),
    path('counties/<int:pk>/edit/', views.county_update, name='county_edit'),
    path('counties/<int:pk>/delete/', views.county_delete, name='county_delete'),
]
