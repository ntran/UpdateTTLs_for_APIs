import httplib
import json

BASE_URL = 'api2.dynect.net'
api = '/REST/SSHFPRecord'

def SSHFPRecord_put(data, ttl, zone, fqdn, token):
    params = {}
    params['rdata'] = {}
    params['rdata']['algorithm'] = data['rdata']['algorithm']
    params['rdata']['fptype'] = data['rdata']['fptype']
    params['rdata']['fingerprint'] = data['rdata']['fingerprint']
    params['ttl'] = ttl
    params = json.JSONEncoder().encode(params)

    conn = httplib.HTTPSConnection(BASE_URL)
    conn.request('PUT', api + '/' + zone + '/' + fqdn + '/' + str(data['record_id']), params, headers = {'Content-type': 'application/json', 'Auth-Token': token})
    
    res = conn.getresponse()
    result = json.loads(res.read())

    if result['status'] == 'failure':
	print 'ERROR - Cannot update record:', data['record_type'], '-', data['rdata']['algorithm'], data['rdata']['fptype'], data['rdata']['fingertype']