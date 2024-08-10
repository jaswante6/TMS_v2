from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Task, TaskAssignment, Comment



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    # users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

