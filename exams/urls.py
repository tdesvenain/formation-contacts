from django.conf.urls import url
from django.urls import path, reverse

from exams import views

urlpatterns = [
    path('', views.ExamsList.as_view(), name='exam-list'),
    path('courses', views.CoursesList.as_view(), name='course-list'),
    path('exam/<int:pk>/', views.ExamNotesView.as_view(), name='exam-notes-list'),
    path('student/<int:pk>/', views.StudentCourses.as_view(), name='student-courses'),
]
