from django.shortcuts import render, redirect

from .apod_api import ApodClass


class ApodHttpMethodsMixin():
	model = None
	form_class = None
	template_name = ''
	apod_class = ApodClass

	def get(self, request):
		apod_data = self.apod_class().get_apod_data()
		try:
			apod_object = self.model.objects.get(
				date = apod_data.get('date'),
			)
		except self.model.DoesNotExist:
			apod_object = None
		context = {
			'date_form': self.form_class(),
			'apod_data': apod_data,
			'apod_object': apod_object,
		}
		return render(request, self.template_name, context)

	def post(self, request):
		form = self.form_class(request.POST)
		apod_data = self.apod_class().get_data_for_requested_date(request.POST)
		try:
			apod_object = self.model.objects.get(
				date = apod_data.get('date'),
			)
		except self.model.DoesNotExist:
			apod_object = None

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
