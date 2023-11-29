from django.urls import path
from .views import (
    PersonListAPIView, PersonRetrieveAPIView, PersonCreateAPIView, PersonDestroyAPIView,
    TaskListAPIView, TaskRetrieveAPIView, TaskCreateAPIView, TaskDestroyAPIView
)

urlpatterns = [
    path('person/list/', PersonListAPIView.as_view(), name='person_list'),
    path('person/<int:pk>/retrieve', PersonRetrieveAPIView.as_view(), name='person_detail'),
    path('person/create/', PersonCreateAPIView.as_view(), name='person_create'),
    path('person/<int:pk>/destroy', PersonDestroyAPIView.as_view(), name='person_delete'),
    path('task/list/', TaskListAPIView.as_view(), name='task_list'),
    path('task/<int:pk>/retrieve', TaskRetrieveAPIView.as_view(), name='task_detail'),
    path('task/create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('task/<int:pk>/destroy', TaskDestroyAPIView.as_view(), name='task_delete'),
]
