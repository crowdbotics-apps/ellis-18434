from django.conf import settings
from django.db import models


class Events(models.Model):
    "Generated Model"
    title = models.TextField()
    location = models.ForeignKey(
        "home.Location", on_delete=models.CASCADE, related_name="events_location",
    )
    date = models.DateField()
    time = models.TimeField()


# Create your models here.
