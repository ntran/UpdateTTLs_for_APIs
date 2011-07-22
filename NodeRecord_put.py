'''
Update the TTLs of all the records in a node
Return: Update a list of Records
'''
import httplib
import json
import Record_put.AAAARecord_put
import Record_put.ARecord_put
import Record_put.CNAMERecord_put
import Record_put.DHCIDRecord_put
import Record_put.DNAMERecord_put
import Record_put.DNSKEYRecord_put
import Record_put.DSRecord_put
import Record_put.KEYRecord_put
import Record_put.LOCRecord_put
import Record_put.MXRecord_put
import Record_put.NSAPRecord_put
import Record_put.NSRecord_put
import Record_put.PTRRecord_put
import Record_put.PXRecord_put
import Record_put.RPRecord_put
import Record_put.SPFRecord_put
import Record_put.SRVRecord_put
import Record_put.SSHFPRecord_put
import Record_put.TXTRecord_put
import zone_put

BASE_URL = 'api2.dynect.net'

RECORD_MODULES = {'AAAARecord': Record_put.AAAARecord_put, 'ARecord': Record_put.ARecord_put, 'CNAMERecord': Record_put.CNAMERecord_put, 'DHCIDRecord': Record_put.DHCIDRecord_put, 'DNAMERecord': Record_put.DNAMERecord_put, 'DNSKEYRecord': Record_put.DNSKEYRecord_put, 'DSRecord': Record_put.DSRecord_put,'KEYRecord': Record_put.KEYRecord_put, 'LOCRecord': Record_put.LOCRecord_put, 'MXRecord': Record_put.MXRecord_put, 'NSAPRecord': Record_put.NSAPRecord_put, 'NSRecord': Record_put.NSRecord_put, 'PTRRecord': Record_put.PTRRecord_put, 'PXRecord': Record_put.PXRecord_put, 'RPRecord': Record_put.RPRecord_put, 'SPFRecord': Record_put.SPFRecord_put, 'SRVRecord': Record_put.SRVRecord_put, 'SSHFPRecord': Record_put.SSHFPRecord_put, 'TXTRecord': Record_put.TXTRecord_put}

RECORD_TYPES = {'AAAARecord': 'AAAARecord', 'ARecord': 'ARecord', 'CNAMERecord': 'CNAMERecord', 'DHCIDRecord': 'DHCIDRecord', 'DNAMERecord': 'DNAMERecord', 'DNSKEYRecord': 'DNSKEYRecord', 'DSRecord': 'DSRecord', 'KEYRecord': 'KEYRecord', 'LOCRecord': 'LOCRecord', 'MXRecord': 'MXRecord', 'NSAPRecord': 'NSAPRecord', 'NSRecord': 'NSRecord', 'PTRRecord': 'PTRRecord', 'PXRecord': 'PXRecord', 'RPRecord': 'RPRecord', 'SPFRecord': 'SPFRecord', 'SRVRecord': 'SRVRecord', 'SSHFPRecord': 'SSHFPRecord', 'TXTRecord': 'TXTRecord'}

def NodeRecord_put(record_list, new_ttl, zone, fqdn, token):
	for i in range(0, len(record_list)):
		data = getRecordInfo(record_list[i][0], record_list[i][1], zone, fqdn, token)
		call_keyword = data['record_type'] + 'Record'
		#Update TTLs of every record is list
		call = getattr(RECORD_MODULES[call_keyword], RECORD_TYPES[call_keyword] + '_put')
		call(data, new_ttl, zone, fqdn, token)
		zone_put.zone_put('publish', zone, token)

##Get the record's data
##Return: record['data']
def getRecordInfo(rec_type, rec_id, zone, fqdn, token):
	conn = httplib.HTTPSConnection(BASE_URL)
	conn.request('GET', '/REST/' + rec_type + 'Record/' + zone + '/' + fqdn +  '/' + str(rec_id), '', headers = {'Content-type': 'application/json', 'Auth-Token': token})

	res = conn.getresponse()
	result = json.loads(res.read())
	return result['data']