from django.conf.urls import url
from django.urls import path, reverse

from persons import views

urlpatterns = [
    path('', views.PersonList.as_view(), name='person-list'),
    path('create/', views.PersonCreate.as_view(), name='person-create'),
    path('<slug:slug>/', views.PersonDetail.as_view(), name='person-detail'),
    path('<slug:slug>/edit', views.PersonUpdate.as_view(), name='person-update'),
    path('<slug:slug>/delete', views.PersonDelete.as_view(), name='person-delete'),
]
