from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=10, default="Medium") 
    price = models.IntegerField(default=0)  
    description = models.TextField(default="No description") 
    notes = models.TextField()