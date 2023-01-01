from django.db import models
from accounts.models import User

class Room(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_rooms')
    title = models.CharField(max_length=200)
    participants = models.ManyToManyField(User)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.creator}"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, models.CASCADE, null=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"Sent by {self.sender}"
