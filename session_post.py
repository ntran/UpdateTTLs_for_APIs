import json
import httplib

BASE_URL = 'api2.dynect.net'
api = '/REST/Session'

    
def session_post(name, userid, password):
        params = {}
        params['customer_name'] = name
        params['user_name'] = userid
        params['password']= password
        login = json.JSONEncoder().encode(params)
    
        conn = httplib.HTTPSConnection(BASE_URL)
        conn.request('POST', api, login, {'Content-type': 'application/json'})
        res = conn.getresponse()
    
        content = res.read()
        result = json.loads(content)

        if result['status'] == 'success': 
            	return result['data']['token']
        else:
		return 0 





