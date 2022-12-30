from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length = 10)
    body = models.TextField()

    def __str__(self):
        return self.title