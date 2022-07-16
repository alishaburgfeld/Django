from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    email=models.EmailField(max_length=255,
    unique=True,)

USERNAME_FIELD="email"
REQUIRED_FIELDS=[]

class Task(models.Model):
    category=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    due_date=models.DateField(null=True)
    priority=models.IntegerField(null=True)
    user=models.ForeignKey(AppUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('category', 'description'))