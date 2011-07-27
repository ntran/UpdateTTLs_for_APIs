'''
Update all the record provided in the input file
'''

# Python libraries
import os
import sys

# Modules
import NodeRecord_get
import NodeRecord_put
import NodeList_get
import session_post

## Update the new_ttls of all the node in a file
## Return: Updated new_ttls
def Updatenew_ttls():

	# Get login information
	file = raw_input("\nPlease enter your input_file's directory: ")
	file = open(file, 'r')
	name, username, pwd = file.readline().strip().split('|')
	zone = file.readline().strip()
	token = session_post.session_post(name, username, pwd)
	if token == 0:
		sys.exit('ERROR: Invalid login information.\n')

	# Start updating 
	for line in file:
		
		if '|' in line:
			fqdn, new_ttl, recursive, old_ttl = line.strip().split('|')
		else:
			continue
		
		print '\n<Node>  -  <Record Type>  -  <Record Data>'

                _rec_list = []

		# If 'y', update all the subnodes, otherwise update the node only
		if recursive == 'y':

			#Get a list of nodes from fqdn
			_list = []
			_list = NodeList_get.NodeList_get(_list, 0, zone, fqdn, token)		

			#Get a list of records in the node(s)
			for i in _list:
				_rec_list = NodeRecord_get.NodeRecord_get(old_ttl, _rec_list, zone, i, token)

		else:
			_rec_list = NodeRecord_get.NodeRecord_get(old_ttl, _rec_list, zone, fqdn, token)

		_request = raw_input("\nThese records' TTLs will be changed. Do you wish to continue? (y/n) ")
		if _request == 'y':
			NodeRecord_put.NodeRecord_put(_rec_list, new_ttl, zone, fqdn, token)
		print '----- Node:', fqdn, '. Update Completed. ------------'

<<<<<<< HEAD
	os.system("find . -name '*.pyc' -delete")	#Clean up *.pyc files
=======
	os.system("rm -r */*.pyc")	#Clean up *.pyc files
	os.system("rm *.pyc")
>>>>>>> 4d51fa7dcca5bb51a88e65e1ca8cf5733b9fe4e6

## Run program
Updatenew_ttls()
 
