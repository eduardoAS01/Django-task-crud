from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    end_at = models.DateField(blank=True,null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title