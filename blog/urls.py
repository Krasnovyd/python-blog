from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post__list, name='post__list'),
]