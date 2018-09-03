#!/usr/bin/env python

from pyEthOS import pyEthOS as ethos
import requests
import json

from config import ethosUrl
from log_helper import get_logger


l = get_logger('ethosapi')

def ethosapi():
	
	PANEL_NAME = ethosUrl()
	DEBUG = False

	#api = ethos.EthOS_API(PANEL_NAME, debug=DEBUG)


	try:
		api = ethos.EthOS_API(PANEL_NAME, debug=DEBUG)
	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit(1)


	#req = requests.get('http://altaiu.ethosdistro.com')
	#req2 = req.json()
	apiReq = api.get_summary()

	dump = json.dumps(apiReq)
	data = json.loads(dump)





if __name__ == "__main__":

	ethosapi()



