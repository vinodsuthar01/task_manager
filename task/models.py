from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    discription = models.TextField()
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('progress','In Progress'),
        ('done','Completed'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,default='Pending')
    PRIORITY_CHOICES = [
        ('high','High'),
        ('medium','Medium'),
        ('low','Low'),
    ]
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)