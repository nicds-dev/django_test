from rest_framework import serializers
from .models import Person, Task

class PersonSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    
    class Meta:
        model = Person
        fields = ['id', 'name', 'last_name', 'document_type', 'document_number', 'email', 'tasks']
    
    def get_tasks(self, obj):
        tasks = obj.tasks.all()
        return tasks.values_list('title', 'description', 'deadline_date')

class TaskSerializer(serializers.ModelSerializer):
    person = serializers.SlugRelatedField(slug_field='name', queryset=Person.objects.all())

    class Meta:
        model = Task
        fields = '__all__'