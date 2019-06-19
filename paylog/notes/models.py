from django.db import models
from django.utils import timezone

class MakeNotes(models.Model):
    note = models.CharField(max_length=200, default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note