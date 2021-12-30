from django.shortcuts import render, redirect
from django.http import Http404

from pprint import pprint


class GetApodDataOr404Mixin:
	apod_class = None

	def get_apod_data(self, request=None):
		if request.method == 'GET' or request is None:
			apod_data = self.apod_class().get_apod_data()
		elif request.method == 'POST':
			apod_data = self.apod_class().get_apod_data_for_requested_date(request.POST)

		if apod_data is None:
			raise Http404('APOD data could not be retrived!')
		print(f'Recived:\n{apod_data}')
		return apod_data


class GetOrCreateApodMixin:
	model = None

	def get_or_create_apod(self, data):
		apod_object = self.model.objects.get_or_create(
			title = data.get('title'),
			date = data.get('date'),
			json_data = data,
		)
		# Debugging porpuse
		if apod_object[1]:
			print('Apod Object Created!')
		else:
			print('Apod Object Got!')

		return apod_object[0]

	def get_or_create_apod_list(self, apod_data_list):
		apod_list = []
		for apod_data in apod_data_list:
			apod_list.append(
				self.get_or_create_apod(apod_data)
			)
		return apod_list



class ApodHttpMethodsMixin(GetOrCreateApodMixin, GetApodDataOr404Mixin):
	model = None
	apod_class = None
	form_class = None
	template_name = ''

	def get(self, request):
		apod_data = self.get_apod_data(request)
		context = {
			'date_form': self.form_class(),
			'apod_data': apod_data,
			'apod_object': self.get_or_create_apod(apod_data),
		}
		return render(request, self.template_name, context)

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			apod_data = self.get_apod_data(request)
			context = {
				'date_form': form,
				'apod_data': apod_data,
				'apod_object': self.get_or_create_apod(apod_data)
			}
		else:
			apod_data = self.get_apod_data()
			context = {
				'apod_data': apod_data,
				'date_form': self.form_class(),
				'apod_object': self.get_or_create_apod(apod_data),
			}
		return render(request, self.template_name, context)


class ApodGridMixin(GetOrCreateApodMixin):

	def get(self, request):
		""" Renders a grid containing the last 30 APODs. """
		apod_data_list = self.apod_class().get_apod_data_for_grid()
		apod_list = self.get_or_create_apod_list(apod_data_list)

		context = {
			'apod_list': apod_list,
		}
		return render(request, self.template_name, context)


class ApodListMixin:
	testing_api = 'https://api.nasa.gov/planetary/apod?api_key=am8Cb93MAtrqcC1bUjrxcqV7Aai1OEqZHpuV1rpx&start_date=2021-12-22&end_date=2021-12-27'

	def get(self, request):
		""" Get the last 30 APOD. """
		apod_data_list = self.apod_class().get_apod_data(self.testing_api)
		context = {
			'apod_list': apod_data_list,
		}
		return render(request, self.template_name, context)
