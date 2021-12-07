import os

from . import apod_parser
from . import apod_local
from . import apod_api


def apod_index():
	API = apod_api.main_api()
	filepath = apod_local.get_file_name()

	# Check wether the corresponding fie does not exist or if it is empty
	if not os.path.isfile(filepath) or not os.stat(filepath).st_size > 0:
		# Retrive APOD data, save it to the corresponding file and returned it
		data = apod_parser.get_data(API)
		apod_local.save_data(data, filepath)
		return data

	# if the corresponding file exist, then read its data
	return apod_local.get_data(filepath)


if __name__ == '__main__':
	from pprint import pprint
	pprint(apod_index())
