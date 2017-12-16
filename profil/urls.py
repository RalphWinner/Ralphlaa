from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^/edit/(?P<profil_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^/(?P<profil_id>[0-9]+)/$', views.details, name='details'),
]