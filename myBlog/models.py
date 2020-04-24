from django.db import models
from django.utils import timezone
from  django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(max_length=1000)
	posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User,on_delete=models.CASCADE,)
	image = models.ImageField(null = True, blank=True)


	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})





	
