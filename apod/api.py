import os, json, urllib.request, environ, requests
from datetime import datetime, timedelta

env = environ.Env()
environ.Env.read_env()


class DateProcessorsMixin:
	"""
	The methdos in this class are intented to be use in ApiClass.
	Note: all methods return string(s) date formated as '2021-12-22'
	"""
	def get_date_for_today(self):
		return str(datetime.now()).split()[0]

	def get_date_from_request(self, request):
		"""
		Precesses POST request and return the requested date.
		"""
		date = [
			request['date_year'],
			request['date_month'],
			request['date_day'],
		]
		date = [e if len(e) > 1 else f'0{e}' for e in date]
		return f'{date[0]}-{date[1]}-{date[2]}'

	def get_date_range(self, start=None, end=None, days=None):
		"""
		Given date objects, returns string dates for a range.
		"""
		days = days if days is not None else 7 # for eight dates
		if not (start and end):
			end = datetime.now()
			start = end - timedelta(days)
		elif start and not end:
			end = start + timedelta(days)
		elif end and not start:
			start = end - timedelta(days)
		return str(start).split()[0], str(end).split()[0]


class ApiProcessorMixin(DateProcessorsMixin):
	"""
	Generate API urls for diferente methods and options such as:
	* date
	* range date
	Note: This class must be use in conjunction with DateProcessorsMixin
	otherwise, methdos such as self.get_date_from_request()
	will raise AttributeError.
	"""
	API = env('API_KEY')

	def get_api_for_date(self, date):
		return f'{self.API}&date={date}'

	def get_api_for_date_in_post_request(self, post_request):
		"""
		post_request must be a POST request such as:
		request.POST pass throught Views
		"""
		date = self.get_date_from_request(request)
		return self.get_api_for_date(date)

	def get_api_for_date_range(self, start=None, end=None, days=None):
		start, end = self.get_date_range(start, end, days)
		return f'{self.API}&start_date={start}&end_date={end}'


class DataRetrivererMixin:

	def get_data_from_api(self, API):
		try:
			with urllib.request.urlopen(API) as data:
				return json.loads(data.read().decode())
		except urllib.error.URLError as error:
			print('Data could not be retrived. Check your internet'
				  f'connection.\n Raised error: {error}')
			raise urllib.error.URLError


class DataProcessorsMixin(ApiProcessorMixin, DataRetrivererMixin):

	def get_apod_data(self, API=None):
		API = self.API if API is None else API
		return self.get_data_from_api(API)

	def get_apod_data_for_str_date(self, date):
		API = self.get_api_for_date(date)
		return self.get_data_from_api(API)

	def get_apod_data_for_requested_date(self, post_request):
		API = self.get_api_for_requested_date(post_request)
		return self.get_data_from_api(API)

	def get_apod_data_for_date_range(self, start, end):
		API = self.get_api_for_date_range(start, end)
		return self.get_data_from_api(API)

	def get_apod_data_for_default_date_range(self):
		API = self.get_api_for_date_range()
		return self.get_data_from_api(API)


class ApiClass(DataProcessorsMixin):
	"""
	Inherit this class to work with the APOD API.
	"""
	pass
