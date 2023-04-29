import sys
import project

while True:
    print("\nWelcome to the Crowd-funding Projects Menu :))")

    print("1- Create project")
    print("2- View all projects")
    print("3- Edit project")
    print("4- Delete project")
    print("5- Search for project by date")
    print("6- Exit")
    choice = input("Enter your choice: ")

    if choice == "1":  # create
     project.create_project()
    elif choice == "2":  # view
         project.view_projects()
    elif choice == "3":  # edit
         project.edit_project()
    elif choice == "4":  # delete
         project.delete_project() 
    elif choice == "5":  # search
         project.search_project()     
    elif choice == "6":
     print("BYE:)))")
     sys.exit()
    else:
        print("Invalid choice. Please try again.")