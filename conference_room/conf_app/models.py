from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.PositiveIntegerField()
    projector = models.BooleanField()
    availability = models.BooleanField(default=True)

class Book(models.Model):
    book_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)

    class Meta:
        unique_together = ('book_date', 'room')