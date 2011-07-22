import httplib
import json

BASE_URL = 'api2.dynect.net'
api = '/REST/KEYRecord'

def KEYRecord_get(old_ttl, zone, fqdn, rec_id, token):
    conn = httplib.HTTPSConnection(BASE_URL)
    conn.request('GET', api + '/' + zone + '/' + fqdn + '/' + str(rec_id), '', headers = {'Content-type': 'application/json', 'Auth-Token': token})

    res = conn.getresponse()
    result = json.loads(res.read())

    if result['status'] == 'success':
        if rec_id == '':
	    return result['data']
	#If the TTLs match, Print the record's info for user
	if ((old_ttl > 0) and (old_ttl == result['data']['ttl'])) or (old_ttl <= 0):
	    print fqdn, '-', result['data']['record_type'], '-', result['data']['rdata']['algorithm'], result['data']['rdata']['flags'], result['data']['rdata']['protocol'], result['data']['rdata']['public_key']
	    return result['data']['record_type'], result['data']['record_id']
    else:
        return 0
