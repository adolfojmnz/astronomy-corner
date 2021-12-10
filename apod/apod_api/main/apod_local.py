import json, os, time
from datetime import datetime


def get_file_name(str_date=None):
	"""
		Returns the filename for the given date object or,
		if str_date is None, returns the filename for current date.
	"""
	if str_date is None:
		str_date = str(datetime.utcnow()).split()[0]
	base_dir = os.path.abspath('./apod/apod_api/retrived_data')
	filename = f'{str_date}.json'
	return f'{base_dir}/{filename}'


def save_data(data, filepath):
	"""
		Saves the data in a json file for later use.
	"""
	with open(filepath, 'w') as f:
		json.dump(data, f)


def get_data(filepath):
	"""
		Returns the data read in the json file specified in filepath.
	"""
	with open(filepath) as f:
		return json.loads(f.read())


if __name__ == '__main__':
	from pprint import pprint
	pprint(get_data(get_file_name()))
