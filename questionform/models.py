from django.db import models

# Create your models here.
class QuestionOne(models.Model):
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text

class QuestionTwo(models.Model):
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text

class QuestionThree(models.Model):
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text
