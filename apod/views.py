from django.views import View

from .models import Apod
from .forms import ApodDateForm

from .api import ApiClass
from .utils import ApodViewMixin, ApodGridMixin, ApodListMixin


class ApodView(View, ApodViewMixin):
	model = Apod
	api_class = ApiClass
	form_class = ApodDateForm
	template_name = 'apod/apod.html'


class ApodGrid(View, ApodGridMixin):
	model = Apod
	api_class = ApiClass
	template_name = 'apod/apod_grid.html'


class ApodList(View, ApodListMixin):
	api_class = ApiClass
	template_name = 'apod/apod_list.html'
