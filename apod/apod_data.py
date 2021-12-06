import os
import urllib.request, json

KEY = 'am8Cb93MAtrqcC1bUjrxcqV7Aai1OEqZHpuV1rpx'
API = f'https://api.nasa.gov/planetary/apod?api_key={KEY}'


def get_data(API, filepath=None):
	try:
		if filepath is None:
			raise FileNotFoundError
		with open(filepath) as json_file:
			data = json.loads(json_file.read())
			return data
	except FileNotFoundError:
		with urllib.request.urlopen(API) as data:
			data = json.loads(data.read().decode())
			return data
	except urllib.error.URLError as error:
		print('Data could not be loaded. Check your internet connection.' +
			 f'Error raised: {error}')


def apod_index():
	filepath = f"{os.path.abspath('./apod')}/apod.json"
	return get_data(API, filepath)


if __name__ == '__main__':
	from pprint import pprint
	pprint(apod_index())
