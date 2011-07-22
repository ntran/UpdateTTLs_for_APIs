import httplib
import json

BASE_URL = 'api2.dynect.net'
api = '/REST/LOCRecord'

def LOCRecord_put(data, ttl, zone, fqdn, token):
    params = {}
    params['rdata'] = {}
    params['rdata']['altitude'] = data['rdata']['altitude']
    params['rdata']['horiz_pre'] = data['rdata']['horiz_pre']
    params['rdata']['latitude'] = data['rdata']['latitude']
    params['rdata']['longitude'] = data['rdata']['longitude']
    params['rdata']['size'] = data['rdata']['size']
    params['rdata']['version'] = data['rdata']['version']
    params['rdata']['vert_pre'] = data['rdata']['vert_pre']
    params['ttl'] = ttl
    params = json.JSONEncoder().encode(params)

    conn = httplib.HTTPSConnection(BASE_URL)
    conn.request('PUT', api + '/' + zone + '/' + fqdn + '/' + str(data['record_id']), params, headers = {'Content-type': 'application/json', 'Auth-Token': token})
    
    res = conn.getresponse()
    result = json.loads(res.read())

    if result['status'] == 'failure':
	print 'ERROR - Cannot update record:', data['record_type'], '-', data['rdata']['altitude'], data['rdata']['horiz_pre'], data['rdata']['latitude'], data['rdata']['longitude'], data['rdata']['size'], data['rdata']['version'], data['rdata']['vert_pre']