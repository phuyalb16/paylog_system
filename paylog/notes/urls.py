from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_view, name='note_view'),
]

