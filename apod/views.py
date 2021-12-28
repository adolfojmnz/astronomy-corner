from django.views import View

from .models import Apod
from .forms import ApodDateForm
from .utils import ApodHttpMethodsMixin


class ApodView(View, ApodHttpMethodsMixin):
	model = Apod
	form_class = ApodDateForm
	template_name = 'apod/apod.html'
