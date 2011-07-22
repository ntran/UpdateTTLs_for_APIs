import httplib
import json

BASE_URL = 'api2.dynect.net'
api = '/REST/PXRecord'

def PXRecord_put(data, ttl, zone, fqdn, token):
    params = {}
    params['rdata'] = {}
    params['rdata']['preference'] = data['rdata']['preference']
    params['rdata']['map822'] = data['rdata']['map822']
    params['rdata']['mapx400'] = data['rdata']['mapx400']
    params['ttl'] = ttl
    params = json.JSONEncoder().encode(params)

    conn = httplib.HTTPSConnection(BASE_URL)
    conn.request('PUT', api + '/' + zone + '/' + fqdn + '/' + str(data['record_id']), params, headers = {'Content-type': 'application/json', 'Auth-Token': token})
    
    res = conn.getresponse()
    result = json.loads(res.read())

    if result['status'] == 'failure':
	print 'ERROR - Cannot update record:', data['record_type'], '-', data['rdata']['preference'], data['rdata']['map822'], data['rdata']['mapx400']