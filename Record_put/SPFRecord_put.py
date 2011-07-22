import httplib
import json
import SPFRecord_editData

BASE_URL = 'api2.dynect.net'
api = '/REST/SPFRecord'

def SPFRecord_put(data, ttl, zone, fqdn, token):
    params = {}
    params['rdata'] = {}
    params['rdata']['txtdata'] = data['rdata']['txtdata']
    params['ttl'] = ttl
    params = json.JSONEncoder().encode(params)

    conn = httplib.HTTPSConnection(BASE_URL)
    conn.request('PUT', api + '/' + zone + '/' + fqdn + '/' + str(data['record_id']), params, headers = {'Content-type': 'application/json', 'Auth-Token': token})
 
    res = conn.getresponse()
    result = json.loads(res.read())

    if result['status'] == 'failure':
	print 'ERROR - Cannot update record:', data['record_type'], '-', data['rdata']['txtdata']