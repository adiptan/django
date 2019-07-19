from django.db import models
from django.utils import timezone

class Details(models.Model):
    model = models.CharField(max_length=100)
    details = models.TextField()
    mileage = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
