from django.conf import settings
from django.db import models
from django.utils import timezone


class Details(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.CharField(max_length=200)
    item = models.TextField()
    # bought_date = models.DateTimeField(default=timezone.now)
    bought_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author

