from django import forms

from .models import Apod


class ApodDateForm(forms.Form):
	date = forms.DateField(
		label='Select A Date',
		widget=forms.SelectDateWidget,
	)

	def __str__(self):
		return self.date


class ApodSaveForm(forms.ModelForm):

	class Meta:
		model = Apod
		fields = '__all__'

	def __str__(self):
		return self.date
