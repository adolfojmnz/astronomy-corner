from django.urls import path

from .views import index

app_name = 'apod'
urlpatterns = [
	path('', index, name='index'),
]
