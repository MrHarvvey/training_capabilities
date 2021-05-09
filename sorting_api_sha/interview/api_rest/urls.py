from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('zadanie1/', views.zadanie1, name="zadanie1"),
	path('zadanie2/', views.zadanie2, name="zadanie2"),
]
