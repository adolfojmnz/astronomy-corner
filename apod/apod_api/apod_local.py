import json, os
from datetime import datetime


def get_file_name():
	base_dir = os.path.abspath('./apod/apod_api/retrived_data')
	filename = str(datetime.utcnow()).split()[0]
	return f'{base_dir}/{filename}.json'


def save_data(filepath, data):
	with open(filepath, 'w') as f:
		json.dump(data, f)


def get_data(filepath):
	with open(filepath) as f:
		return json.loads(f.read())


if __name__ == '__main__':
	print(get_file_name())
