from django.db import models

class Cheesecake(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=10)
    price = models.IntegerField()
    description = models.TextField()
    notes = models.TextField()