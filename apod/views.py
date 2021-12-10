from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from .forms import APODDate

from .apod_api.main.apod_data import apod_main
from .apod_api.main.apod_api import get_requested_date


def index(request):
	template_name = 'apod/index.html'
	context = {
		'apod_data': render_requested_apod(request),
		'form': render_requested_form(request),
	}
	return render(request, template_name, context)


def render_requested_form(request):
	if request.method == 'POST':
		form = APODDate(request.POST)
		if form.is_valid():
			return form
		return APODDate()
	if request.method == 'GET':
		return APODDate()


def render_requested_apod(request):
	if request.method == 'POST':
		date = get_requested_date(request.POST)
	else:
		date = str(timezone.now() - timedelta(hours=4)).split()[0]
	print(date)
	return apod_main(str_date=date)
