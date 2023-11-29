from django.urls import path
from .views import (
    PersonListAPIView, PersonRetrieveAPIView, PersonCreateAPIView, PersonDestroyAPIView,

)

urlpatterns = [
    path('person/list/', PersonListAPIView.as_view(), name='person_list'),
    path('person/<int:pk>/retrieve', PersonRetrieveAPIView.as_view(), name='person_detail'),
    path('person/create/', PersonCreateAPIView.as_view(), name='person_create'),
    path('person/<int:pk>/destroy', PersonDestroyAPIView.as_view(), name='person_delete'),
]
