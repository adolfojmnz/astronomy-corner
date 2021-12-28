from django.views import View

from .models import Apod
from .forms import ApodDateForm, ApodCreateForm
from .utils import ApodHttpMethodsMixin, ApodCreateMixin

from .apod_api import ApodClass


class ApodView(View, ApodHttpMethodsMixin):
	model = Apod
	apod_class = ApodClass
	form_class = ApodDateForm
	template_name = 'apod/apod.html'

class ApodCreate(View, ApodCreateMixin):
	model = Apod
	apod_class = ApodClass
	form_class = ApodCreateForm
	template_name = 'apod/apod.html'
