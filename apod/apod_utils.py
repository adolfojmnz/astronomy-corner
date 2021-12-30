from django.shortcuts import render, redirect
from django.http import Http404

from datetime import datetime, timedelta
from pprint import pprint


class GetApod:
	"""
	Get or create Apod object(s) for the given str date
	formated as 2021-12-22.
	"""
	model = None
	apod_class = None

	def get_or_create_apod(self, date):
		try:
			apod_object = self.model.objects.get(date=date)
		except self.model.DoesNotExist:
			try:
				data = self.apod_class().get_apod_data_for_str_date(date)
			except:
				print('GetApod.get_or_create_apod:\nData could not be retrived!')
				return None # Do something with this, perhaps
			apod_object = self.model.objects.create(
				title = data.get('title'),
				date = data.get('date'),
				image = None,
				json_data = data,
			)
		return apod_object

	def get_or_create_apod_list(self, start, end):
		start = datetime.strptime(start, '%Y-%m-%d')
		end = datetime.strptime(end, '%Y-%m-%d')
		delta = end - start

		apod_list = []
		date = start
		while delta > timedelta(0):
			str_date = str(date).split()[0]
			apod_list.append(
				self.get_or_create_apod(str_date)
			)
			date += timedelta(1)
			delta -= timedelta(1)
		return apod_list
