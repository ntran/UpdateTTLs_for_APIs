import NodeRecord_get

def UpdateTTLs_node(zone, fqdn, ttl, request, token):
	record_list = []
	resource = ANYRecord_get.ANYRecord_get(zone, fqdn, token)	#List of record_resources
	for i in resource:
		temp, temp0, record_type, temp1, temp2, record_id = i.split('/')
		record_list = NodeRecord_get.NodeRecord_get(zone, fqdn, token)

	_request = raw_input(fqdn + " - These records's TTLs will be changed. Do you want to continue? (y or n)")	

	return record_list