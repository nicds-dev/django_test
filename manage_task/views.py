from rest_framework import generics, status
from rest_framework.response import Response
from .models import Person, Task
from .serializers import PersonSerializer, TaskSerializer

"""
    CRUD for Person model
"""
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

class PersonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()
    
    def put(self, request, pk):
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Person updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        return Person.objects.all()

    def destroy(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
            person.delete()
            return Response({'message': 'Person deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Person.DoesNotExist:
            return Response({'message': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

"""
    CRUD for Task model
"""

class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
    
        # Filter by deadline date
        deadline_date = self.request.query_params.get('deadline_date', None)

        if deadline_date:
            queryset = queryset.filter(deadline_date=deadline_date)

        # Filter by range of deadline dates
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if start_date and end_date:
            queryset = queryset.filter(deadline_date__range=[start_date, end_date])

        # Filter by person (type and document number)
        document_type = self.request.query_params.get('document_type', None)
        document_number = self.request.query_params.get('document_number', None)
        
        if document_type and document_number:
            queryset = queryset.filter(person__document_type=document_type, person__document_number=document_number)

        return queryset
    
class TaskRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.all()
    
class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.all()
    
    def put(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()
    
    def destroy(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)