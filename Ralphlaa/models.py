from django.contrib.auth.models import User
from django.db import models


class Profil(models.Model):
    user = models.OneToOneField(User)
    about = models.TextField(default=None)
    telephone = models.CharField(max_length=8, default='0')
    sexe = models.CharField(max_length=10, default='0')
    naissance = models.DateField()
    profil = models.FileField(upload_to='Profil')

    def __str__(self):
        return self.user.username

