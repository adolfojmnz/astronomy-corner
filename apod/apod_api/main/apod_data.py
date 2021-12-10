import os, time
try:
	from . import apod_parser, apod_local, apod_api
except ImportError:
	import apod_parser, apod_local, apod_api


def apod_main(API=None, str_date=None):
	if API is None:
		API = apod_api.apod_main()
	filepath = apod_local.get_file_name(str_date)

	# Check wether the corresponding file does not exist or if it is empty
	if not os.path.isfile(filepath) or not os.stat(filepath).st_size > 0:
		print(f'requesting data for {str_date}...')
		t0 = time.time()
		data = apod_parser.get_data(API, str_date) # Retrive APOD data, save it to the corresponding file and return it
		t1 = time.time()
		print(f'Data retrived in {t1-t0:.4f} seconds')
		apod_local.save_data(data, filepath)
		return data

	# if the corresponding file exist, then read its data
	t0 = time.time()
	data = apod_local.get_data(filepath)
	t1 = time.time()
	print(f'Data retrived in {t1-t0:.4f} seconds')
	return data


if __name__ == '__main__':
	from pprint import pprint
	pprint(apod_main())
