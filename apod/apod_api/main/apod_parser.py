import urllib.request, json

def get_data(API, date=None):
	if date:
		API = f'{API}&date={date}'
	try:
		with urllib.request.urlopen(API) as data:
			return json.loads(data.read().decode())
	except urllib.error.URLError as error:
		print('Data could not be retrived. Check your internet connection.\n' +
			 f'Raised error: {error}')


if __name__ == '__main__':
	from pprint import pprint
	from apod_api import main_api

	pprint(get_data(main_api()))
