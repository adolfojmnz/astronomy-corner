from django.shortcuts import render, redirect
from django.http import Http404

from .apo_utils GetApod


class ApodViewMixin(GetApod):
	model = None
	api_class = None
	form_class = None
	template_name = ''

	def get(self, request):
		context = {
			'form': self.form_class(),
			'apod': sel.get_apod()
		}
		return render(request, self.template_name, context)

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			date = self.api_class().get_date_from_request(request.POST)
			context = {
				'form': form,
				'apod': self.get_apod(date),
			}
			return render(request, self.template_name, context)
		else:
			context = {
				'form': self.form_class(),
				'apod': self.get_apod(),
			}
			return render(request, self.template_name, context)


class ApodGridMixin(GetApod):

	def get(self, request):
		pass

	def post(self, request):
		pass


class ApodListMixin(GetApod):

	def get(self, request):
		pass

	def post(self, request):
		pass
