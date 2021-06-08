from django.urls import path
from .views import PeopleAPIView, safe_people_db, safe_people2, bitcoin_cost, hash_search, hash_del, list_persons

urlpatterns = [
	#Leave as empty string for base url
	path('zadanie1/', PeopleAPIView.as_view(), name="zadanie1"),
	path('zadanie2/', safe_people_db, name='safe_people_db'),
	path('zadanie3/', safe_people2, name='safepeople2'),
	path('zadanie4/', bitcoin_cost, name='safepeople3'),
	path('hash/', hash_search, name='hash_search'),
	path('hash_del/', hash_del, name='hash_del'),
	path('list_persons/', list_persons, name='list_persons'),
]
