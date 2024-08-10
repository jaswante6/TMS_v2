from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, through='TaskAssignment', related_name='tasks_assigned')
    assigned_to = models.EmailField()

    def __str__(self):
        return self.title

class Meta:
    db_table = "task"

    def mark_as_completed(self):  
        if self.status == 'In Progress':
            self.status = 'Completed'
            self.completion_time = timezone.now()
            self.save()
        else:
            raise ValueError("Task is not in 'In Progress' status and cannot be marked as completed.")  

    def is_overdue(self):
        return self.due_date < timezone.now() and self.status != 'Completed'

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Meta:
    db_table = "project"

class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, related_name='assignments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='assignments', on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.title} assigned to {self.user.username}"
    

class Meta:
     unique_together = ('task', 'user')  


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"

class Meta:
    db_table = "comment"

