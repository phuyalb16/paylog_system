from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('persondetails/', views.search, name='search_person'),
    path('allusers/', views.all_users, name='all_users')
]

