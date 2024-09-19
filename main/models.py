from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=10, default="") 
    price = models.IntegerField(default=0)  
    description = models.TextField(default="") 
    notes = models.TextField()