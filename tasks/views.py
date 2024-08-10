from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Task,Project,Comment,TaskAssignment
from .serializers import TaskSerializer,ProjectSerializer,CommentSerializer,TaskAssignmentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from django.core.mail import send_mail



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer    


class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.all()
    serializer_class =    TaskAssignmentSerializer 


@api_view(['POST'])
def complete_task(request, id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        task.mark_as_completed()
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def overdue_tasks(request):
    now = timezone.now()
    overdue_tasks = Task.objects.filter(due_date__lt=now, status__ne='Completed')
    serializer = TaskSerializer(overdue_tasks, many=True)
    for task in overdue_tasks:
        simulate_email_notification(task.assigned_to, task.title)

    return Response(serializer.data, status=status.HTTP_200_OK)

def simulate_email_notification(email, task_title):
    print(f"Simulating sending email to {email} about overdue task: {task_title}")





def simulate_email_notification(email, task_title):
    subject = 'Overdue Task Notification'
    message = f'Your task "{task_title}" is overdue. Please take action.'
    from_email = 'noreply@yourdomain.com'
    
    send_mail(subject, message, from_email, [email])


@api_view(['GET'])
def get_project_progress(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    tasks = project.tasks.all()
    total_tasks = tasks.count()
    if total_tasks == 0:
        return Response({"progress": 0}, status=status.HTTP_200_OK)
    priority_weights = {
        'LOW': 1,
        'MEDIUM': 2,
        'HIGH': 3,
    }
    
    weighted_total = 0
    weighted_completed = 0

    for task in tasks:
        weight = priority_weights[task.priority]
        weighted_total += weight
        if task.status == 'COMPLETED':
            weighted_completed += weight

    progress = (weighted_completed / weighted_total) * 100

    return Response({"progress": progress}, status=status.HTTP_200_OK)

