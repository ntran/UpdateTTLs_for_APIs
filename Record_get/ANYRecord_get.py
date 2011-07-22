import httplib
import json

BASE_URL = 'api2.dynect.net'
api = '/REST/ANYRecord'

def ANYRecord_get(zone, fqdn, token):
    	conn = httplib.HTTPSConnection(BASE_URL)
    	conn.request('GET', api + '/' + zone + '/' + fqdn, '', headers = {'Content-type': 'application/json', 'Auth-Token': token})

    	res = conn.getresponse()
    	result = json.loads(res.read())

    	if result['status'] == 'success':
        	return result['data']
    	else:
        	return 'ERROR: Cannot retrieve records from ' + fqdn
