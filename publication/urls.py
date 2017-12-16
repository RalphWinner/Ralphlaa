from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^/liste_des_publications', views.liste_des_publications, name='liste_des_publications'),
    url(r'^/(?P<publication_id>[0-9]+)', views.details, name='details'),
    url(r'^/modification/(?P<publication_id>[0-9]+)', views.modification, name='modification'),
    url(r'^/effacer/(?P<publication_id>[0-9]+)', views.effacer, name='effacer'),
]
