from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auth_products')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(default="", blank=True)
    price = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=20, default="Medium")
    notes = models.TextField(blank=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    stock = models.IntegerField(default=0)  # Tambahkan kolom stock di sini
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.size} - {self.price}"