from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length = 10)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    value = models.TextField() #ここに科目名を入力 Subjectのtitleと一致するかに使用
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.value