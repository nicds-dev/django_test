from django.urls import path
from .views import (
    PersonListAPIView, PersonRetrieveAPIView, PersonCreateAPIView, PersonUpdateAPIView, PersonDestroyAPIView,
    TaskListAPIView, TaskRetrieveAPIView, TaskCreateAPIView, TaskUpdateAPIView, TaskDestroyAPIView
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Task Management Docs.",
      default_version='v1.0.0',
      description="Technical test, API REST for task management",
      terms_of_service="https://nicds.onrender.com/",
      contact=openapi.Contact(email="nikolasdurango@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('person/list/', PersonListAPIView.as_view(), name='person_list'),
    path('person/<int:pk>/retrieve', PersonRetrieveAPIView.as_view(), name='person_detail'),
    path('person/create/', PersonCreateAPIView.as_view(), name='person_create'),
    path('person/<int:pk>/update', PersonUpdateAPIView.as_view(), name='person_update'),
    path('person/<int:pk>/destroy', PersonDestroyAPIView.as_view(), name='person_delete'),
    path('task/list/', TaskListAPIView.as_view(), name='task_list'),
    path('task/<int:pk>/retrieve', TaskRetrieveAPIView.as_view(), name='task_detail'),
    path('task/create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('task/<int:pk>/update', TaskUpdateAPIView.as_view(), name='task_update'),
    path('task/<int:pk>/destroy', TaskDestroyAPIView.as_view(), name='task_delete'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]