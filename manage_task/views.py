from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from datetime import datetime
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

        # Get the filters from the query parameters
        filters = {}
    
        # Filter by deadline date
        deadline_date_str = self.request.query_params.get('deadline_date', None)
        if deadline_date_str:
            try:
                filters['deadline_date'] = datetime.strptime(deadline_date_str, '%Y-%m-%d')
            except (ValueError, TypeError) as e:
                raise ParseError(f'Invalid deadline date format or value: {e}. Please use YYYY-MM-DD format.')
            
        # Filter by range of deadline dates
        start_date_str = self.request.query_params.get('start_date', None)
        end_date_str = self.request.query_params.get('end_date', None)

        if start_date_str and end_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
                filters['deadline_date__range'] = [start_date, end_date]
            except (ValueError, TypeError) as e:
                raise ParseError(f'Invalid deadline date range format: {e}. Please use YYYY-MM-DD format.')
            
        # Filter by person (type and document number)
        document_type = self.request.query_params.get('document_type', None)
        document_number = self.request.query_params.get('document_number', None)

        if document_type is not None and document_number is not None:
            filters['person__document_type'] = document_type
            filters['person__document_number'] = document_number
        
        # Apply the filters
        if filters:
            queryset = queryset.filter(**filters)

        if not queryset.exists():
            raise NotFound('No tasks found for the given filters.')
        
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