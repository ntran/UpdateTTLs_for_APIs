The program read the user INPUT_FILE and update all the NODEs listed.

----- PROGRAM EXPLANATION -----
The program will ask you to enter your file's directory.
Then it lists all the Records in side 1 node, ask if you want to continue updating (y or n).
If you confirm 'y', it will update all the Record with the new_ttl written in the file.
Then it proceed to the next node in the file, and do the updating until the end of the file.

----- INPUT_FILE FORMAT -----
customer_name|username|password
zone
node_name_1|new_ttl_1|update_all_its_child_node?(y or n)
node_name_2|new_ttl_2|update_all_its_child_node?(y or n)

Example: 
input_file:  C:\Users\your_username\A Folder\filename.txt (Windows) 
	       /Users/your_username/A Folder/filename.txt (Mac)
	    
dyn-john|johnsmith|mypassword
Example.com
test1.example.com|3600|y
test2.example.com|60|n
test3.example.com|1800|y


----- RUN PROGRAM -----
Run: 	Directory\UpdateTTLs\UpdateTTLs.py (Windows)
	Directory/UpdateTTLs/UpdateTTLs.py (Mac)


