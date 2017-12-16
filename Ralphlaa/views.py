from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Profil
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from . import Ralph_function as R
from django.contrib.auth.decorators import login_required
from .forms import ContactForm


def test(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return HttpResponseRedirect('/')

    return render(request, 'pages/test.html', {
        'form': form,
    })



def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def konekte(request):
    if request.user.pk != None:
        return HttpResponseRedirect('success/'+str(request.user.pk))


    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('modpas')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            id = User.objects.get(username = user).pk
            return HttpResponseRedirect('success/' + str(id))
        else:
            return HttpResponseRedirect('/konekte/')

    return render(request, 'pages/konekte.html')

def Enskri(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        about = request.POST.get('about')
        sexe = request.POST.get('sexe')
        telephone = request.POST.get('telephone')
        date_in_str = request.POST.get('naissance')
        date = datetime.strptime(date_in_str, '%Y-%m-%d')
        profil = request.POST.get('profil')

        user = User.objects.create_user(username, email, password)
        user.first_name = nom
        user.last_name = prenom

        user.save()

        profil = Profil(user=user, about=about, telephone=telephone, sexe=sexe, naissance=date, profil=profil)

        profil.save()

        return HttpResponseRedirect('/konekte/')
    return render(request, 'pages/enskri.html', {})

@login_required(login_url='/konekte/')
def success(request, id):

    users = []

    for u in R.list_user():
        users.append(u)

        
    users.remove(request.user)


    details = {
        'username': User.objects.get(pk=id).username,
        'nom': User.objects.get(pk=id).first_name,
        'prenom': User.objects.get(pk=id).last_name,
        'email': User.objects.get(pk=id).email,
        'profil': User.objects.get(pk=id).profil.profil,
        'telephone': User.objects.get(pk=id).profil.telephone,
        'sexe': User.objects.get(pk=id).profil.sexe,
        'naissance': User.objects.get(pk=id).profil.naissance.strftime('%d %B %Y'),
        'naissance2': User.objects.get(pk=id).profil.naissance.strftime('%Y-%m-%d'),
        'users': users
    }
    return render(request, 'pages/login_success.html', details)


def deconnexion(request):
    logout(request)
    return HttpResponseRedirect('/konekte/')

