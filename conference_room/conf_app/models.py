from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.PositiveIntegerField()
    projector = models.BooleanField()
    availability = models.BooleanField(default=True)


