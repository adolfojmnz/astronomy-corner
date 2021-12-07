import os
import urllib.request, json

KEY = 'am8Cb93MAtrqcC1bUjrxcqV7Aai1OEqZHpuV1rpx'
API = f'https://api.nasa.gov/planetary/apod?api_key={KEY}'


def create_file_name():
	from time import localtime
	filepath = os.path.abspath('./apod/apod_data_json')
	date = [f'{e}' if len(f'{e}') > 1 else f'0{e}' for e in localtime()[:3]]
	return f'{filepath}/apod_data_{date[0]}-{date[1]}-{date[2]}.json'


def create_json_file(data, filepath):
	with open(filepath, 'w') as f:
		json.dump(data, f)
	return data


def get_data(API, filepath=None):
	try:
		if filepath is None:
			raise FileNotFoundError
		with open(filepath) as json_file:
			print('reached')
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
	filepath = create_file_name()

	# Check wether the corresponding fie does not exist or if it is empty
	if not os.path.isfile(filepath) or not os.stat(filepath).st_size > 0:
		# Create the corresponding file with the APOD API data
		return create_json_file(get_data(API), filepath)

	# if the corresponding file exist, then read its data
	return get_data(API, filepath)


if __name__ == '__main__':
	from pprint import pprint
	pprint(apod_index())
