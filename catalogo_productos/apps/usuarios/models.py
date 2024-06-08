from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Usuario(AbstractUser):
    
    biografia = models.CharField(max_length=255, null=True, blank=True)