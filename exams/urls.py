from django.conf.urls import url
from django.urls import path, reverse

from exams import views

urlpatterns = [
    path('', views.ExamsList.as_view(), name='exam-list'),
    path('exam/<int:pk>/', views.ExamNotesView.as_view(), name='exam-notes-list'),
    path('student/<slug:slug>/', views.StudentCourses.as_view(), name='student-courses'),
]
