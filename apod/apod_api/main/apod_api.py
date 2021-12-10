from datetime import datetime, timedelta

try:
	from . date_methods import get_str_date_from_post_request, get_date_range
except ImportError:
	from date_methods import get_str_date_from_post_request, get_date_range

KEY = 'am8Cb93MAtrqcC1bUjrxcqV7Aai1OEqZHpuV1rpx'
API = f'https://api.nasa.gov/planetary/apod?api_key={KEY}'
# "msg": "Date must be between Jun 16, 1995 and Dec 08, 2021.",


def get_api():
	return API


def apod_main(API=None):
	if API is None:
		return get_api()
	return API


def apod_date(date, API=None):
	if API is None:
		API = apod_main()
	return f'{API}&date={date}'

def get_requested_date(request, API=None):
	if API is None:
		API = apod_main()
	return get_str_date_from_post_request(request)


def apod_date_range(API=None, start=None, end=None):
	""" The maximum days range is 5. """
	if API is None:
		API = apod_main()
	start_date, end_date = get_date_range(start, end)
	return f'{API}&start_date={start_date}&end_date={end_date}'


if __name__ == '__main__':
	from test_apod import test_apod_api
	test_apod_api(API, '2021-11-08', '2021-11-13')
