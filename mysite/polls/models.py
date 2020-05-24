from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Useritem(models.Model):
    user_email = models.CharField(max_length=254)
    item_title = models.CharField(max_length=200)
    item_contents = models.TextField()
    count = models.IntegerField(default=0)
