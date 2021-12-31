from django.urls import path

from .views import ApodView, ApodList, ApodGrid


app_name = 'apod'
urlpatterns = [
	path('', ApodView.as_view(), name='apod'),
	path('grid/', ApodGrid.as_view(), name='grid'),
	path('list/', ApodList.as_view(), name='list'),
]
