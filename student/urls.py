from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('student/', views.index),
    path('register/', views.register),
    path('students/', views.students),
    path('student/<int:student_id>/', views.student_detail),
    path('course/',views.course),
]
