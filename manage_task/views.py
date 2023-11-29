from rest_framework import generics, status
from rest_framework.response import Response
from .models import Person, Task
from .serializers import PersonSerializer, TaskSerializer

class PersonListAPIView(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()
    
