Supported Python versions: 2.5, 2.6, 2.7

The program read the user INPUT_FILE and update all the NODEs listed.

----- PROGRAM EXPLANATION -----
The program will ask you to enter your file's directory.
Then it lists all the Records in side 1 node, ask if you want to continue updating (y or n).
If you confirm 'y', it will update all the Record with the new_ttl written in the file.
Then it proceed to the next node in the file, and do the updating until the end of the file.

----- INPUT_FILE FORMAT -----
customer_name|username|password
zone
node_name_1|new_ttl_1|update_all_its_child_node?(y or n)|current_ttl_1(0 if you want to change all TTLs)
node_name_2|new_ttl_2|update_all_its_child_node?(y or n)|current_ttl_2

Example: 
input_file:  C:\Users\your_username\A Folder\filename.txt (Windows) 
	       /Users/your_username/A Folder/filename.txt (Mac)
	    
dyn-john|johnsmith|mypassword
example.com
test1.example.com|3600|y|60		<< Change records whose current TTLs are 60
test2.example.com|60|n|0		<< Change all records TTLs
test3.example.com|1800|y|30		<< Change records whose current TTLs are 30


----- RUN PROGRAM -----
Run: 	Directory\UpdateTTLs\UpdateTTLs.py (Windows)
	Directory/UpdateTTLs/UpdateTTLs.py (Mac)


