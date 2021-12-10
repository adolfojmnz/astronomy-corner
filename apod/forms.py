from django import forms
from django.utils import timezone


class APODDate(forms.Form):
	date = forms.DateField(label='Select A Date', widget=forms.SelectDateWidget)

	def __str__(self):
		return self.date
