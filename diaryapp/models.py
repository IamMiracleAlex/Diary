from django.db import models


class Note(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Note #{self.id}'