import httplib
import json

BASE_URL = 'api2.dynect.net'
api = '/REST/Zone'

def zone_put_publish(serial, serialstyle, zone, zonetype):
    params = {}
    params['publish'] = publish
    params['serial']  = serial
    params['serial_style'] = serialstyle
    params['zone'] = zone
    params['zone_style'] = zonestyle
    params = json.JSONEncoder().encode(params)
    return params

def zone_put(zonechange, zone, token):
    params = {}
    if zonechange == 'freeze':
        params['freeze'] = True
    else:
        if zonechange == 'thaw':
            params['thaw'] = True
        else:
            if zonechange == 'publish':
                params['publish'] = True
    params = json.JSONEncoder().encode(params)
        
    conn = httplib.HTTPSConnection(BASE_URL)
    conn.request('PUT', api + '/' + zone, params, headers = {'Content-type': 'application/json', 'Auth-Token': token})

    res = conn.getresponse()    
    result = json.loads(res.read())

    if result['status'] == 'success':
        return 'SUCCESS'
    else:
        return 'FAIL'
