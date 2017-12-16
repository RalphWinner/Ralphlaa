"""Ralphlaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sevis/', include('sevis.urls'), name='sevis'),
    url(r'^publication', include('publication.urls'), name='publication'),
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^konekte/$', views.konekte, name='Konekte'),
    url(r'^konekte/success/(?P<id>[0-9]+)', views.success, name='success'),
    url(r'^konekte/deconnexion', views.deconnexion, name='deconnexion'),
    url(r'^enskri/$', views.Enskri, name='Enskri'),
    url(r'^profil/', include('profil.urls'), name='profil'),
    url(r'^test/', views.test, name='test'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)