from django.urls import path

from .views import UserCreate, UserDetail


app_name = 'users'
urlpatterns = [
	path('users/create/', UserCreate.as_view(), name='create'),
	path('users/<int:pk>/detail/', UserDetail.as_view(), name='detail'),
]
