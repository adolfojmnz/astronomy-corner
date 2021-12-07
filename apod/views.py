from django.shortcuts import render

from .apod_api.apod_data import apod_index


def index(request):
	template_name = 'apod/index.html'
	context = {'apod_data': apod_index()}
	return render(request, template_name, context)
