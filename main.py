# import modules
import sys
import auth 

# Main program loop
 
print("\nWelcome to the Crowd-funding Console App:))")
print("1- Register")
print("2- Login")
print("3- Exit")
choice = input("Enter your choice: ")

if choice == "1":  # Register
 auth.register()
elif choice == "2":  # Login
 auth.login()
elif choice == "3":
 print("BYE:)))")
 sys.exit()
else:
    print("Invalid choice. Please try again.")