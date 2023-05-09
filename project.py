import datetime
import os
import general
# create project
def create_project():
    id = input("Enter the id of your project: ")
    while not general.validate_id(id):
        print("Re-enter id  ")
        id = input("nter the id of your project: ")

    user_id = input("Enter your id: ")
    while not general.validate_id(user_id):
        print("Re-enter id  ")
        user_id = input("Enter your id: ")
    title = input("Enter the title of your project: ")
   
    # check if  project is unique
    if check_project(id,user_id,title):
         print(f"Project with id {id} and title {title} Already exists..")
         return
   
    details = input("Enter the details of your project: ")
    total_target = float(input("Enter the total target amount for your project: "))
    start_date_str = input("Enter the start date for your project (YYYY-MM-DD): ")
    end_date_str = input("Enter the end date for your project (YYYY-MM-DD): ")
    # Validate start/end date
    try:
        start_date = datetime.datetime.strptime(start_date_str,"%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date_str,"%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter dates in the format YYYY-MM-DD .")
        return
    if start_date >= end_date:
        print("End date must be after start date.")
        return
    
   


    data=f"{id}:{user_id}:{title}:{details}:{total_target}:{start_date}:{end_date}"
    record="id:user_id:title:details:total_target:start_date:end_date"+"\n"
    general.save('projects.txt',data,record)    
    print("Project Scssfully Created")





def check_project(id,user_id,title):
    if os.path.exists('projects.txt'):
      with open('projects.txt', 'r') as file:
            for line in file:
                fields = line.strip().split(':')
                if  fields[0] == id and fields[1] == user_id and fields[2]== title:
                    return True
      file.close()   
    else:
        with open('projects.txt',"a") as file:
            pass
        file.close()    
  
     
#    edit 
def edit_project():
     id = input("Enter the id of your project: ")
     if search_project_id(id) :
        title = input("Enter the title of your project: ")
        details = input("Enter the details of your project: ")
        total_target = float(input("Enter the total target amount for your project: "))
        start_date_str = input("Enter the start date for your project (YYYY-MM-DD): ")
        end_date_str = input("Enter the end date for your project (YYYY-MM-DD): ")
        # Validate start/end date
        try:
          start_date = datetime.datetime.strptime(start_date_str,"%Y-%m-%d").date()
          end_date = datetime.datetime.strptime(end_date_str,"%Y-%m-%d").date()
        except ValueError:
         print("Invalid date format. Please enter dates in the format YYYY-MM-DD .")
         return
        if start_date >= end_date:
         print("End date must be after start date.")
         return
    
        
        with open('projects.txt', 'r') as file:
            lines=file.readlines()
            for i,line in enumerate(lines):
                fields = line.strip().split(':')
                if fields[0]==id:    
                    fields[2]=title
                    fields[3]=details
                    fields[4]=str(total_target)
                    fields[5]=str(start_date)
                    fields[6]=str(end_date)
                    lines[i] = ':'.join(fields) + '\n'

        file.close()
        with open("projects.txt",'w') as file:
            file.writelines(lines)                
        file.close()  
    
        print("Project Updated Succssfully")

     else:
          print("Project not found")
          return     

def search_project_id(id):
     with open("projects.txt",'r') as file:
         for line in file:
              fields=line.strip().split(":")
              stored_id=fields[0]
              if stored_id == id :
                   return True
     file.close()         

# view all projects
def view_projects():
      with open('projects.txt', 'r') as file:
            for line in file:
                print(line,end="")
      file.close() 

#   delete project
def delete_project():
    id =  input("Enter the ID of the project to delete: ")

    # Check if project exists
    status=False
    with open('projects.txt', 'r') as file:
            lines=file.readlines()
            for i,line in enumerate(lines):
                fields = line.strip().split(':')
                if  fields[0] == id :
                    del lines[i]
                    status=True
    with open("projects.txt",'w') as file:
            file.writelines(lines)                
    file.close() 

    # Delete project
    if status:

     print("Project deleted successfully.")
    else:
         print("Project not found")

# serach project by date
def search_project():
      # Get start/end date to search for
    start_date_str = input("Enter the start date to search for (YYYY-MM-DD): ")
    end_date_str = input("Enter the end date to search for (YYYY-MM-DD): ")

    # Validate start/end date
    try:
        start_date = datetime.datetime.strptime(start_date_str,"%Y-%m-%d").date()
        end_date   = datetime.datetime.strptime(end_date_str,"%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter dates in the format YYYY-MM-DD.")
        return
    if start_date >= end_date:
        print("End date must be after start date.")
        return
    print (type(start_date))
    with open("projects.txt",'r') as file:
         l=file.readline()
         for line in file:

              fields=line.strip("\n").split(":")
              start=datetime.datetime.strptime(fields[5],"%Y-%m-%d").date()
              end=datetime.datetime.strptime(fields[6],"%Y-%m-%d").date()
              if start_date >= start and end <= end_date:
                   print(line)
               
    file.close()         