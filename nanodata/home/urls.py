from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
	path('', views.index, name = 'index'),
	path('encode-ton-texte/', views.text_encode, name = 'text_encode'),
	path('rencontres/', views.rencontres, name = 'rencontres'),
	path('team/', views.team, name = 'team'),
	path('partners/', views.partners, name = 'partners'),
	path('post_text/', views.post_text, name = 'post_text'),
]

