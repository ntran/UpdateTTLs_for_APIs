import httplib
import json

BASE_URL = 'api2.dynect.net'
api = '/REST/SRVRecord'

def SRVRecord_put(data, ttl, zone, fqdn, token):
    params = {}
    params['rdata'] = {}
    params['rdata']['port'] = data['rdata']['port']
    params['rdata']['priority'] = data['rdata']['priority']
    params['rdata']['target'] = data['rdata']['target']
    params['rdata']['weight'] = data['rdata']['weight']
    params['ttl'] = ttl
    params = json.JSONEncoder().encode(params)

    conn = httplib.HTTPSConnection(BASE_URL)
    conn.request('PUT', api + '/' + zone + '/' + fqdn + '/' + str(data['record_id']), params, headers = {'Content-type': 'application/json', 'Auth-Token': token})
    
    res = conn.getresponse()
    result = json.loads(res.read())

    if result['status'] == 'failure':
	print 'ERROR - Cannot update record:', data['record_type'], '-', data['rdata']['port'], data['rdata']['priority'], data['rdata']['target'], data['rdata']['weight']