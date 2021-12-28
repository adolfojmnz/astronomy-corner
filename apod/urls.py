from django.urls import path

from .views import ApodView


app_name = 'apod'
urlpatterns = [
	path('', ApodView.as_view(), name='apod'),
]
