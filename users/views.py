from django.views import View

from .models import User
from .forms import UserCreateForm
from .utils import UserCreateMixin, UserDetailMixin


class UserCreate(View, UserCreateMixin):
	model = User
	form_class = UserCreateForm
	template_name = 'users/user_create_form.html'


class UserDetail(View, UserDetailMixin):
	model = User
	template_name = 'users/user_detail.html'
