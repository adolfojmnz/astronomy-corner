from django.urls import path

from .views import ApodView, ApodList


app_name = 'apod'
urlpatterns = [
	path('', ApodView.as_view(), name='apod'),
	path('list/', ApodList.as_view(), name='list'),
]
