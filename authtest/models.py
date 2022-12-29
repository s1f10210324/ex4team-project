from django.db import models
from django.utils import timezone

# Create your models here.
class Folder1(models.Model):
    title = models.CharField(max_length=20) #フォルダーの名前
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now) #フォルダーを作った日
    published_at = models.DateTimeField(blank=True, null=True) 
    like = models.IntegerField(default=0)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Card(models.Model):
    problem = models.TextField()
    answer = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    correct = models.IntegerField(default=0)
    miss = models.IntegerField(default=0)