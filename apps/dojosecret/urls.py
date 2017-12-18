from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^success$", views.success, name="success"),
	url(r"^login$", views.login, name="login"),
	url(r"^register$", views.register, name="register"),
	url(r"^delete", views.delete, name="delete"),
	url(r"^add$", views.add, name="add"),
	url(r"^review$", views.review, name="review"),
	url(r"^user/(?P<id>\d+)", views.user, name="user"),
	url(r"^book/(?P<id>\d+)", views.book, name="book")
]