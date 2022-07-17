# coding=utf-8
import datetime
from functools import wraps

def log_file(function):
	path = 'log/log.log'
	@wraps(function)
	def new_function(*args, **kwargs):
		with open(path, 'a', encoding = 'utf-8') as log_file:
			date = datetime.datetime.now()
			data = f'{date} {new_function.__name__} {args} {kwargs} {log_file}\n'
			log_file.write(data)
			return log_file

	return new_function