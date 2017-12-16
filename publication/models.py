from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class publication(models.Model):
	userr = models.ManyToManyField(User)
	titre = models.CharField(max_length=50)
	tst = models.CharField(null=True, max_length=100)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	email = models.EmailField()
	user = models.CharField(max_length=100)
	edit = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.titre
    	#return str(self.id) + '|' +self.titre + '|' + self.body
