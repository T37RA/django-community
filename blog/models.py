from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from markupfield.fields import MarkupField


class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=750)
	content = MarkupField(default_markup_type='html')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})