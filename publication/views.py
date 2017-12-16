from django.shortcuts import render
from .models import publication as p
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


def home(request):
    return (render(request, 'publication/index.html'))

def liste_des_publications(request):
	if request.method == 'POST':
		user = request.POST.get('name')
		titre = request.POST['subject']
		email = request.POST.get('email')
		body = request.POST.get('message')

		p.objects.create(titre = titre , body = body, email = email, user = user)
		
	publications = p.objects.all()
	return (render(request, 'publication/liste_des_publications.html', {'listP': publications}))

def details(request, publication_id):
	try:
		d = {
		'publication_id': publication_id,
		'titre': p.objects.get(pk=publication_id),
		'body': p.objects.get(pk=publication_id).body,
		'date': p.objects.get(pk=publication_id).date,
		'user': p.objects.get(pk=publication_id).user,
		'email': p.objects.get(pk=publication_id).email,
		'edit': p.objects.get(pk=publication_id).edit,
		}
		return(render(request, 'publication/details.html', d))
	except Exception as e:
		return (render(request, 'publication/liste_des_publications.html'))

	

def modification(request, publication_id):
	if request.method == 'POST':
		d = {
		'titre': p.objects.get(pk=publication_id).titre,
		'body': request.POST.get('message'),
		'user': request.POST.get('name'),
		'email': request.POST.get('email'),
		'date': p.objects.get(pk=publication_id).date,
		}

		pub = p.objects.get(pk = publication_id)
		pub.titre = d['titre']
		pub.body = d['body']
		pub.user = d['user']
		pub.email = d['email']
		pub.save()


		d.update({'edit': p.objects.get(pk=publication_id).edit})

		return(render(request, 'publication/details.html', d))


def effacer(request, publication_id):
	p.objects.filter(pk = publication_id).delete()
	return HttpResponseRedirect('/publication/liste_des_publications/')
