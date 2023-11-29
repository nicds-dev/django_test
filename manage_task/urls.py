from django.urls import path
from .views import (
    PersonListAPIView,

)

urlpatterns = [
    path('person/', PersonListAPIView.as_view(), name='person_list'),
]
