'''
Get a list of children nodes inside a node
Return: The node and its children
'''

import httplib
import json

BASE_URL = 'api2.dynect.net'
api = '/REST/NodeList'

def NodeList_get(_list, count, zone, fqdn, token):
    	#Get a list of children nodes in 1 node
	conn = httplib.HTTPSConnection(BASE_URL)
    	conn.request('GET', api + '/' + zone + '/' + fqdn, '', headers = {'Content-Type': 'application/json', 'Auth-Token': token})
    	res = conn.getresponse()	
    	result = json.loads(res.read())

	#Add the nodes found to the list
	for i in result['data']:
		count += 1
		_list.append(i)

	#Go through the _list, and find there children nodes recursively
	for i in range(count, len(result['data'])):
		NodeList_get(_list, count, zone, result['data'][i], token)

   	if result['status'] == 'failure':
		print 'Cannot retrieve children nodes from', fqdn  
	
    	return _list