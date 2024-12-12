import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Todo(models.Model):

    def __str__(self):
        return self.description + " has priority " + self.priority

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    
    priority_levels = {
            ("L", "LOW"),
            ("M", "MEDIUM"),
            ("H", "HIGH"),
            ("N", "NONE")
    } 
    description = models.CharField(max_length=180)
    priority = models.CharField(max_length=1, choices=priority_levels, default="N")
    pub_date = models.DateTimeField("date published")

