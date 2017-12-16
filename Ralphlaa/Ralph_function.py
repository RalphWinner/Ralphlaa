from django.contrib.auth.models import User



def list_user():
	return User.objects.all()