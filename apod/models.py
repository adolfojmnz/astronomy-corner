from django.db import models
from django.urls import reverse

import os


class GetReversedURL:

	def get_reversed_url(self, urlpattern_name, kwargs=None):
		if kwargs:
			return reverse(urlpattern_name, **kwargs)
		return reverse(urlpattern_name)


class Apod(models.Model, GetReversedURL):
	title = models.CharField(max_length=100)
	date = models.DateField(
		primary_key=True,
		help_text='Date for an APOD',
	)
	image = models.ImageField(
		upload_to="apod/apod_data/images/",
	 	blank=True,
		null=True,
	)
	json_data = models.JSONField()

	def get_absolute_url(self):
		return self.get_reversed_url('apod:apod')

	def get_save_url(self):
		return self.get_reversed_url('apod:save')

	def get_delete_url(self):
		return self.get_reversed_url('apod:delete')

	def __str__(self):
		return f'{self.date}'
