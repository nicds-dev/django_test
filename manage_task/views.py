from rest_framework import generics, status
from rest_framework.response import Response
from .models import Person, Task
from .serializers import PersonSerializer, TaskSerializer

class PersonListAPIView(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()

class PersonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        return Person.objects.all()

class PersonCreateAPIView(generics.CreateAPIView):
    serializer_class = PersonSerializer

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Person created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PersonSerializer
    
    def destroy(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
            person.delete()
            return Response({'message': 'Person deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Person.DoesNotExist:
            return Response({'message': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
