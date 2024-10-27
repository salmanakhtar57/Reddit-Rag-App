from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Questions(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.RESTRICT, null=True)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    question  = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question.title