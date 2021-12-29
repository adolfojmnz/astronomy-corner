from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from pprint import pprint


class GetUserMixin:

	def get_model_object(self, **kwargs):
		return get_object_or_404(
			self.model,
			**kwargs,
		)

	def get_user(self, **kwargs):
		user_object = get_object_or_404(
			self.model,
			**kwargs,
		)
		return user_object


class UserCreateMixin(GetUserMixin):

	def get(self, request):
		context = {
			'form': self.form_class(),
		}
		return render(request, self.template_name, context)

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			new_user = form.save()
			return redirect(new_user)
		context = {
			'form': form,
		}
		return render(request, self.template_name, context)


class UserHttpMixin:

	def get(self, request, **kwargs):
		if kwargs:
			object = self.get_model_object(**kwargs)
			if self.form_class:
				context = {
					'form': self.form_class(instance=object),
					self.model.__name__.lower(): object
				}
			else:
				context = {
					self.model.__name__.lower(): object
				}
		else:
			context = {
				'form': self.form_class()
			}
		return render(request, self.template_name, context)


class UserDetailMixin(GetUserMixin):

	def get(self, request, **kwargs):
		user_object = self.get_user(**kwargs)
		context = {
			'user': user_object,
		}
		return render(request, self.template_name, context)


class UserUpdateMixin(GetUserMixin):

	def get(self, request, **kwargs):
		user_object = self.get_user(**kwargs)
		context = {
			'form': self.form_class(instance=user_object),
			'user': user_object,
		}
		return render(request, self.template_name, context)


	def post(self, request, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			updated_user = form.update()
			return redirect(updated_user)
		context = {
			'form': form,
			'user': self.get_user(**kwargs),
		}
		return render(request, self.template_name, context)


class UserDeleteMixin(GetUserMixin):

	def get(sef, request, **kwargs):
		context = {
			'user': self.get_user(**kwargs)
		}
		return render(request, self.template_name, context)

	def post(self, request, **kwargs):
		user_object = self.get_user(**kwargs)
		user_object.delete()
		return redirect('apod:apod')
