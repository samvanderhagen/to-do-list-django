from django.db import models

# Create your models here.
class Todo(models.Model):

    def __str__(self):
        return self.description + " has priority " + self.priority
    
    priority_levels = {
            ("L", "LOW"),
            ("M", "MEDIUM"),
            ("H", "HIGH"),
            ("N", "NONE")
    } 
    description = models.CharField(max_length=180)
    priority = models.CharField(max_length=1, choices=priority_levels, default="N")
    pub_date = models.DateTimeField("date published")


