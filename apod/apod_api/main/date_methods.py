from datetime import datetime, timedelta


def get_str_date_from_post_request(request=None):
	"""
		Returns the date found in 'request' or, if
		request is None, returns the current date.
	"""
	if request:
		date_list = [
			request['date_year'],
			request['date_month'],
			request['date_day'],
		]
		date = [e if len(e) > 1 else f'0{e}' for e in date_list]
		date = f'{date[0]}-{date[1]}-{date[2]}'
	else:
		date = str(datetime.utcnow()).split()[0]
	return date


def get_date_range(start=None, end=None, days=5):

	if start and end:
		init_date, end_date = start, end
	elif start and not end:
		init_date, end_date = start, start + timedelta(days=days)

	return str(init_date).split()[0], str(end_date).split()[0]


if __name__ == '__main__':
	pass
