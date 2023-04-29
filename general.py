# To get users/projects data
# Assume each first line in file for metadata 
# Actual data start from second line
import os
import re

# Validate id
def validate_id(id):
     pattern = "^\d+$"
     return bool(re.match(pattern, id))

# read data
def read(file_path):
    if os.path.exists(file_path):
        with open(file_path,"r") as file:
                 file.readline() # skip the first line
                 file.seek(0, 1) # move the file pointer to the beginning of the second line
                 data = file.read()  # all file data
                 return data

# Save new user/project
def save(file_path,data,record):
          lines=open(file_path).readlines()
          if os.path.exists(file_path) and len(lines) > 1:
            with open(file_path,"a") as file:
                  file.write(data + '\n')
                  file.close()
          else:
                with open(file_path,"w") as file:
                  file.write(record)
                  file.write(data + '\n')
                  file.close()
                  
