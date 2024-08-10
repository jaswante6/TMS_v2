from django.contrib import admin
from tasks .models import Task,Project,Comment,TaskAssignment

# Register your models here.
admin.site.register(Task),
admin.site.register(Project),
admin.site.register(Comment),
admin.site.register(TaskAssignment)


