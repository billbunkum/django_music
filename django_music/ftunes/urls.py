from django.conf.urls import include, url

from ftunes import views

urlpatterns = [
    url(r'^$', views.albums, name="albums"),
]