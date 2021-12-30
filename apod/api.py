import os, json, urllib.request, environ
from datetime import datetime, timedelta

env = environ.Env()
environ.Env.read_env()

class ApodClass:
	API = env('API_KEY')

	# Methods to get date string
	def get_date_for_today(self):
		return str(datetime.now()).split()[0]

	def get_date_from_request(self, request):
		date = [
			request['date_year'],
			request['date_month'],
			request['date_day'],
		]
		date = [e if len(e) > 1 else f'0{e}' for e in date]
		return f'{date[0]}-{date[1]}-{date[2]}'

	def get_date_range(self, start=None, end=None, days=None):
		""" Given date objects, returns string dates for a range. """
		days = 5 if days is None else days
		if start and end:
			pass
		else:
			if not (start and end):
				end = datetime.now()
				start = end - timedelta(days)
			elif start:
				end = start + timedelta(days)
			elif end:
				start = end - timedelta(days)
		return str(start).split()[0], str(end).split()[0]


	# Methods to get APOD's api
	def get_api(self):
		return self.API

	def get_api_for_date(self, date):
		return f'{self.API}&date={date}'

	def get_api_for_requested_date(self, request):
		date = self.get_date_from_request(request)
		return self.get_api_for_date(date)

	def get_api_for_date_range(self, start=None, end=None, days=None):
		start, end = self.get_date_range(start, end, days)
		return f'{self.API}&start_date={start}&end_date={end}'


	# Methods to precess retrived data
	def get_abs_filepath(self, str_date=None):
		str_date = str(datetime.now()).split()[0] if str_date is None else str_date
		base_dir = os.path.abspath('./apod/apod_data/retrived_data')
		return f'{base_dir}/{str_date}.json'

	def save_data_on_disk(self, data, abs_filepath):
		with open(abs_filepath, 'w') as f:
			json.dump(data, f)
			return True
		return False

	def read_data_from_file(self, abs_filepath):
		with open(abs_filepath) as f:
			return json.loads(f.read())
		return False


	# Methods to retrive data
	def get_data_from_api(self, API):
		try:
			with urllib.request.urlopen(API) as data:
				return json.loads(data.read().decode())
		except urllib.error.URLError as error:
			print('Data could not be retrived. Check your internet'
				  f'connection.\n Raised error: {error}')
			raise urllib.error.URLError


	# Methods to load the data
	def get_apod_data(self, API=None, str_date=None):
		abs_filepath = self.get_abs_filepath(str_date)
		API = self.API if API is None else API

		if not (os.path.isfile(abs_filepath) and os.stat(abs_filepath).st_size > 0):
			print(f'Requesting data from:\n {API}')
			data = self.get_data_from_api(API)
			self.save_data_on_disk(data, abs_filepath)
		else:
			print(f'Reading data from:\n {abs_filepath}')
			data = self.read_data_from_file(abs_filepath)

		return data

	def get_apod_data_for_requested_date(self, request):
		""" Returns data for date found in request.POST.date. """
		API = self.get_api_for_requested_date(request)
		return self.get_data_from_api(API)

	def get_apod_data_for_date_range(self, start=None, end=None):
		start = datetime.now() if start is None else start
		API = self.get_api_for_date_range(start, end)
		apod_data_range = self.get_data_from_api(API)

		for apod_data in apod_data_range:
			abs_filepath = self.get_abs_filepath(apod_data.get('date'))
			if not (os.path.isfile(abs_filepath) and os.stat(abs_filepath).st_size > 0):
				self.save_data_on_disk(apod_data, abs_filepath)
		return apod_data_range

	def get_apod_data_for_grid(self):
		""" Returns the data for the last 30 APODs. """
		end = datetime.now()
		start = end - timedelta(days=30)
		return self.get_apod_data_for_date_range(start, end)


if __name__ == '__main__':
	apod_class = ApodClass()

	start, end = apod_class.get_date_range(days=30)
	api = apod_class.get_api_for_date_range(start, end)
	print(apod_class.get_data_from_api(api))
