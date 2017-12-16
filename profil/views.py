from django.shortcuts import render
from publication.models import publication as p
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.


def details(request, profil_id):
	name = p.objects.get(pk = profil_id).user
	email = p.objects.get(pk = profil_id).email
	info = {'name': name, 'email': email, 'profil_id': profil_id}
	return render(request, 'profil/index.html', info)

def edit(request, profil_id):
	name = request.POST.get('name')
	email = request.POST.get('email')

	person = p.objects.get(pk = profil_id)

	person.user = name
	person.email = email

	person.save()

	return HttpResponseRedirect('/profil/'+str(profil_id))

