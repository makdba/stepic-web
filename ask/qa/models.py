from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField(blank=True)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User, related_name = 'likes')


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeFiels()
	question = models.ForeignKey(Question)
	author = models.GoreignKey(User)

