#  encoding utf-8
from log_file import log_file
from log_file_path import log_file_path


@log_file
def function(a, b, c):
	return a, b, c


function(123, 234, 345)

PATH = 'new_log/file.log'


@log_file_path(PATH)
def function_new(a, b, c):
	return a, b, c


function_new(2, 3, 4)