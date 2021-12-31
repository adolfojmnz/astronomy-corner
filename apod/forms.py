from django import forms

from .models import Apod


class DateInput(forms.DateInput):
    input_type = 'date'


class ApodDateForm(forms.Form):
	date = forms.DateField(
		widget = DateInput(),
	)

	def __str__(self):
		return self.date
