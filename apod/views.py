from django.views import View
from django.shortcuts import render

from .models import Apod
from .forms import ApodDateForm
from .utils import ApodHttpMethodsMixin, ApodListMixin, ApodGridMixin

from .api import ApodClass



class ApodView(View, ApodHttpMethodsMixin):
	model = Apod
	apod_class = ApodClass
	form_class = ApodDateForm
	template_name = 'apod/apod.html'


class ApodGrid(View, ApodGridMixin):
	model = Apod
	apod_class = ApodClass
	template_name = 'apod/apod_grid.html'


class ApodList(View, ApodListMixin):
	apod_class = ApodClass
	template_name = 'apod/apod_list.html'
