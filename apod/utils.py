from django.shortcuts import render, redirect
from django.http import Http404

from pprint import pprint


class GetOrCreateApodMixin:
	model = None

	def get_or_create_apod(self, data):
		return self.model.objects.get_or_create(
			title = data.get('title'),
			date = data.get('date'),
			json_data = data,
		)[0]


class ApodHttpMethodsMixin(GetOrCreateApodMixin):
	model = None
	apod_class = None
	form_class = None
	template_name = ''

	def get(self, request):
		apod_data = self.apod_class().get_apod_data()
		if apod_data is None:
			raise Http404('Sorry, the APOD could not be retrived. Try again later!')
		pprint(apod_data)

		apod_object = self.get_or_create_apod(apod_data)
		print(apod_object)

		context = {
			'date_form': self.form_class(),
			'apod_data': apod_data,
			'apod_object': apod_object,
		}
		return render(request, self.template_name, context)

	def post(self, request):
		form = self.form_class(request.POST)

		apod_data = self.apod_class().get_data_for_requested_date(request.POST)
		if apod_data is None:
			raise Http404('Sorry, the APOD could not be retrived. Try again later!')
		pprint(apod_data)

		apod_object = self.get_or_create_apod(apod_data)
		print(apod_object)

		if form.is_valid():
			print(form.cleaned_data)
			context = {
				'date_form': form,
				'apod_data': apod_data,
				'apod_object': apod_object,
			}
		else:
			context = {
				'apod_data': self.apod_class().get_apod_data(),
				'date_form': self.form_class(),
				'apod_object': apod_object,
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
