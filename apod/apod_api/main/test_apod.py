from test_module import test


def test_apod_api(API, start_date, end_date):
	import apod_api

	# response variables
	date_response = f'{API}&date={start_date}'
	date_range_response = f'{API}&start_date={start_date}&end_date={end_date}'

	print(test(apod_api.apod_main(API) == API))
	print(test(apod_api.apod_date(start_date, API) == date_response))
	print(test(apod_api.apod_date_range(API, start=start_date, end=end_date) == date_range_response))


def test_date_methods(API, request, requested_date, start_date, end_date):
	import date_methods

	# response variables
	expected_date_range = start_date, end_date

	print(test(date_methods.get_str_date_from_post_request(request) == requested_date))
	print(test(date_methods.get_date_range(start=start_date, end=end_date) == expected_date_range))


if __name__ == '__main__':
	request = {'csrfmiddlewaretoken': ['HrOdWfk96VeR1uX23uhbXvNrXSCMM4WhedEBeipF4uhS9Gv4m6O5lgLu2cEcN47h'], 'date_month': ['1'], 'date_day': ['1'], 'date_year': ['2021']}
	requested_date = '1564-07-22'
	start_date = '2011-11-07'
	end_date = '2011-11-12'
	API = 'API-EXAMPLE'

	test_apod_api(API, start_date, end_date)
	test_date_methods(API, request, requested_date, start_date, end_date)
