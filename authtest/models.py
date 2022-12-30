from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length = 10)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    question = models.TextField()
    answer = models.TextField()