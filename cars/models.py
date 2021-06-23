from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    position = models.PositiveIntegerField(default=0, unique=True)
    color = models.CharField(max_length=30)
