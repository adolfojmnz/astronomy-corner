from django.urls import path

from .views import ApodView, ApodCreate


app_name = 'apod'
urlpatterns = [
	path('', ApodView.as_view(), name='apod'),
	path('create/', ApodCreate.as_view(), name='create'),
]
