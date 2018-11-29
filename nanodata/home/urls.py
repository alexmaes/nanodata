from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

app_name = "home"

urlpatterns = [
			url(r'^$', views.index, name = 'index'),
			]