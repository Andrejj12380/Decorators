# coding=utf-8
import datetime
from functools import wraps

def log_file(function):
	path = 'log/log.log'
	@wraps(function)
	def new_function(*args, **kwargs):
		with open(path, 'a', encoding = 'utf-8') as log_file:
			date = datetime.datetime.now()
			result = function(*args)
			data = f'{date} {new_function.__name__} {args} {kwargs} {result}\n'
			log_file.write(data)
			return result

	return new_function