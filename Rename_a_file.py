import os

try:
    file_path = raw_input("Enter file path: ")
    old_file_name = raw_input("Enter old file name(with extension): ")            
    new_file_name = raw_input("Enter new file name(with extension): ")
    old_file = file_path +'/' + old_file_name 
    new_file = file_path +'/' + new_file_name 
    result = os.rename(old_file,new_file)
    if(result == None):
        print "Success"
except Exception as e:
    s = str(e)
    if(("Error 2" in s) == True ):
        print "Error:: Old file name does not exist"
    else:
        print "Error:: File path does not exist"
    
