from django.db import models
from django.utils import timezone

class Details(models.Model):
    name = models.CharField(max_length=200)
    amount = models.FloatField()
    item = models.TextField()
    bought_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
