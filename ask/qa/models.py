from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(blank=True, null=True)
	author = models.ForeignKey(User, related_name='question_author_set', null=True, blank=True)
	likes = models.ManyToManyField(User, related_name = 'question_likes_set')

def get_url(self):
	return reverse('question_info', kwargs= {'id':self.id})

def __unicode__(self):
	return self.title


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)

