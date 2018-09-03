#!/usr/bin/env python


import yaml

from log_helper import get_logger


l = get_logger('config')

#this class is the parser for yml file


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

def ethosUrl():
	s = parser()
	sa = s['ethosLink']
	
	l.info('ethOS panel name = ' + sa )
	return str(sa)


if __name__ == "__main__":
	#print (parser())
	s = parser()

	