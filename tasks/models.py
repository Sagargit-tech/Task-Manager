from django.db import models

from django.contrib.auth.models import User, AbstractUser, Group, Permission


# class User(AbstractUser):
#     groups = models.ManyToManyField(Group, related_name='custom_user_set')
#     user_permissions = models.ManyToManyField(
#         Permission, related_name='custom_user_set')

#     def __str__(self):
#         return self.username

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.IntegerField(
        choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(
        User, related_name='tasks', on_delete=models.CASCADE)


class TaskList(models.Model):
    name = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User, related_name='task_lists', on_delete=models.CASCADE)


class Comment(models.Model):
    task = models.ForeignKey(
        Task, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
