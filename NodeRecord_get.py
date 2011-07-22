'''
Get all the available record in a Node
Return: a list of Records
'''

import Record_get.AAAARecord_get
import Record_get.ARecord_get
import Record_get.CNAMERecord_get
import Record_get.DHCIDRecord_get
import Record_get.DNAMERecord_get
import Record_get.DNSKEYRecord_get
import Record_get.DSRecord_get
import Record_get.KEYRecord_get
import Record_get.LOCRecord_get
import Record_get.MXRecord_get
import Record_get.NSAPRecord_get
import Record_get.NSRecord_get
import Record_get.PTRRecord_get
import Record_get.PXRecord_get
import Record_get.RPRecord_get
import Record_get.SPFRecord_get
import Record_get.SRVRecord_get
import Record_get.SSHFPRecord_get
import Record_get.TXTRecord_get

RECORD_MODULES = [Record_get.AAAARecord_get, Record_get.ARecord_get, Record_get.CNAMERecord_get, Record_get.DHCIDRecord_get, Record_get.DNAMERecord_get, Record_get.DNSKEYRecord_get, Record_get.DSRecord_get, Record_get.KEYRecord_get, Record_get.LOCRecord_get, Record_get.MXRecord_get, Record_get.NSAPRecord_get, Record_get.NSRecord_get, Record_get.PTRRecord_get, Record_get.PXRecord_get, Record_get.RPRecord_get, Record_get.SPFRecord_get, Record_get.SRVRecord_get, Record_get.SSHFPRecord_get, Record_get.TXTRecord_get]

RECORD_TYPES = ['AAAARecord', 'ARecord', 'CNAMERecord', 'DHCIDRecord', 'DNAMERecord', 'DNSKEYRecord', 'DSRecord', 'KEYRecord', 'LOCRecord', 'MXRecord', 'NSAPRecord', 'NSRecord', 'PTRRecord', 'PXRecord', 'RPRecord', 'SPFRecord', 'SRVRecord', 'SSHFPRecord', 'TXTRecord']

def NodeRecord_get(record_list, zone, fqdn, token):
	for i in range(0, len(RECORD_MODULES)):
		call = getattr(RECORD_MODULES[i], RECORD_TYPES[i] + '_get')

		#Search for records in each type, using 'GET' function
		source = call('', zone, fqdn, token)
		if source != 0:
			for j in source:
				#Match record_ids with its address
				data = j.split('/')
				if data != []:
					temp, temp0, _type, temp1, temp2, j = j.split('/')

				#Retrieve the record_type and its ID, add them to the record_list
				_type, _id = call(str(j), zone, fqdn, token)
				record_list.append((_type, _id))

	return record_list
	

