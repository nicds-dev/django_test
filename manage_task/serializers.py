from rest_framework import serializers
from .models import Person, Task

class PersonSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    
    class Meta:
        model = Person
        fields = ['id', 'name', 'last_name', 'document_type', 'document_number', 'email', 'tasks']
    
    def get_tasks(self, obj):
        tasks = Task.objects.filter(person_id=obj.id)
        task_data = TaskSerializer(tasks, many=True).data

        # Remove the 'person' field from the task data only when person's model is listed
        for task in task_data:
            task.pop('person', None)

        return task_data

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'