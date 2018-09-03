#!/usr/bin/env python


import yaml

from log_helper import get_logger


l = get_logger('rigbots')

#this class is the parser for yml file
class Config:

	def parser():

		filename = "../settings.yml"

		with open(filename, 'r') as stream:
			try:
				l.info('Parsing Config Files')
				l.info('Opening {}'.format(filename))
				l.info('{} Successfully Read'.format(filename))
				val = yaml.load(stream)
			#	print(val)
			except yaml.YAMLError as exc:
				l.fatal(
                    'Error parsing file {filename}: {exc}. Please fix and try '
                    'again.'.format(filename=filename, exc=exc))
			#	print(exc)

		return val



	if __name__ == "__main__":
		print (parser())
		