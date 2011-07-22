import httplib
import json

BASE_URL = 'api2.dynect.net'
api = '/REST/DSRecord'

def DSRecord_put(data, ttl, zone, fqdn, token):    
    params = {}
    params['rdata'] = {}
    params['rdata']['algorithm'] = data['rdata']['algorithm']
    params['rdata']['digest'] = data['rdata']['digest']
    params['rdata']['digtype'] = data['rdata']['digtype']
    params['rdata']['keytag'] = data['rdata']['keytag']
    params['ttl'] = ttl
    params = json.JSONEncoder().encode(params)

    conn = httplib.HTTPSConnection(BASE_URL)
    conn.request('PUT', api + '/' + zone + '/' + fqdn + '/' + str(data['record_id']), params, headers = {'Content-type': 'application/json', 'Auth-Token': token})
    
    res = conn.getresponse()
    result = json.loads(res.read())

    if result['status'] == 'failure':
	print 'ERROR - Cannot update record:', data['record_type'], '-', data['rdata']['algorithm'], data['rdata']['digest'], data['rdata']['digtype'], data['rdata']['keytag']