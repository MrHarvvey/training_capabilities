from django.urls import path
from .views import PeopleAPIView, safe_people, safe_people2

urlpatterns = [
	#Leave as empty string for base url
	path('zadanie1/', PeopleAPIView.as_view(), name="zadanie1"),
	path('zadanie2/', safe_people, name='safepeople'),
	path('zadanie3/', safe_people2, name='safepeople2'),
	path('zadanie4/', safe_people2, name='safepeople2'),
]
