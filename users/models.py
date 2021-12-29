from django.db import models
from django.urls import reverse
from django.shortcuts import get_object_or_404

from apod.models import Apod


class GetReversedURL:

	def get_reversed_url(self, urlpattern_name):
		return reverse(
			urlpattern_name,
			kwargs = {'pk': self.pk}
		)


class User(models.Model, GetReversedURL):
	name = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	birthdate = models.DateField()
	apods = models.ManyToManyField(
		Apod,
		blank=True,
	)

	class Meta:
		 ordering = ['name']

	def get_create_url(self):
		return self.get_reversed_url('users:create')

	def get_absolute_url(self):
		return self.get_reversed_url('users:detail')

	def get_update_url(self):
		return self.get_reversed_url('users:update')

	def get_delete_url(self):
		return self.get_reversed_url('users:delete')

	def __str__(self):
		return f'{self.lastname.title()}, {self.name.title()}'
