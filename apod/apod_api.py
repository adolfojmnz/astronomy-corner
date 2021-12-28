import json, os, urllib
from datetime import datetime, timedelta


class ApodDate:

	def get_date_for_today(self):
		date = str(timezone.now()).split()[0]
		return date

	def get_date_from_request(self, request):
		date_list = [
			request['date_year'],
			request['date_month'],
			request['date_day'],
		]
		date = [e if len(e) > 1 else f'0{e}' for e in date_list]
		return f'{date[0]}-{date[1]}-{date[2]}'

	def get_date_range(self, start=None, end=None, days=5):
		if start and end:
			init_date, end_date = start, end
		elif start and not end:
			init_date, end_date = start, start + timedelta(days=days)

		return str(init_date).split()[0], str(end_date).split()[0]


class ApodApi(ApodDate):
	KEY = 'am8Cb93MAtrqcC1bUjrxcqV7Aai1OEqZHpuV1rpx'
	API = f'https://api.nasa.gov/planetary/apod?api_key={KEY}'

	def get_api():
		return self.API

	def get_api_for_date(self, date):
		return f'{self.API}&date={date}'

	def get_api_for_requested_date(self, request):
		date = self.get_date_from_request(request)
		return self.get_api_for_date(date), date

	def get_api_for_date_range(self, start=None, end=None, days=5):
		start, end = self.get_date_range(start, end, days)
		return f'{self.API}&start_date={start}&end_date={end}'


class ApodProcesssData:

	def get_abs_filepath(self, str_date=None):
		if str_date is None:
			str_date = str(datetime.utcnow()).split()[0]
		base_dir = os.path.abspath('./apod/apod_data/retrived_data')
		filename = f'{str_date}.json'
		return f'{base_dir}/{filename}'

	def save_data_on_localfile(self, data, abs_filepath):
		with open(abs_filepath, 'w') as f:
			json.dump(data, f)

	def read_data_from_localfile(self, abs_filepath):
		with open(abs_filepath) as f:
			return json.loads(f.read())


class ApodDataRetriver:

	def get_data_from_api(self, API):
		try:
			with urllib.request.urlopen(API) as data:
				return json.loads(data.read().decode())
		except urllib.error.URLError as error:
			print('Data could not be retrived. Check your internet'
				  f'connection.\n Raised error: {error}')


class ApodClass(ApodApi, ApodProcesssData, ApodDataRetriver):

	def get_apod_data(self, API=None, date=None):
		abs_filepath = self.get_abs_filepath(date)
		API = API if API is not None else self.API
		print(API)

		if not (os.path.isfile(abs_filepath) and os.stat(abs_filepath).st_size > 0):
			print(f'Requesting data from API...')
			data = self.get_data_from_api(API)
			self.save_data_on_localfile(data, abs_filepath)
		else:
			print('Reading data from local file...')
			data = self.read_data_from_localfile(abs_filepath)

		return data

	def get_data_for_requested_date(self, request):
		""" request must be request.POST. """
		API, date = self.get_api_for_requested_date(request)
		return self.get_apod_data(API, date)

	def get_data_for_requested_date_range(self):
		pass
