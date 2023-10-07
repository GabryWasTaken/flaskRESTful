import requests 
import json

BASE = "http://127.0.0.1:5000/" # base url

def menu():
    while True:
        print("#######################")
        print("### User RestfulAPI ###")
        print("#######################")
        print("1. Get user data")
        print("2. Create user")
        print("3. Get all users")
        print("4. Exit")
        print("#######################")
        print("#######################")
        try:
            choice = input("Enter your choice: ")
            choice=int(choice)
        except:
            choice=int(77)
        match choice:
            case 1:
                user_id = input("Enter user id: ")
                response = requests.get(BASE + "user/" + user_id)

                try:
                    print(response.json())
                except json.decoder.JSONDecodeError as e:
                    print("No user found")

            case 2:
                username = input("Enter username: ")
                email = input("Enter email: ")
                password = input("Enter password: ")

                data = {"username":username,
                        "email":email,
                        "password":password}
                
                #headers --> to tell the server what type of data we are sending
                headers = {'Content-type': 'application/json' , 'Accept': 'text/plain'}

                response = requests.post(BASE + "create_user",
                                          data=json.dumps(data) , 
                                          headers=headers)
                try:
                    print(response.json())
                except json.decoder.JSONDecodeError as e:
                    print("Error decoding JSON:", e)

            case 3:
                response = requests.get(BASE + "user")

                try:
                    print(response.json())
                except json.decoder.JSONDecodeError as e:
                    print("Error decoding JSON:", e)
                    
            case 4:
                break
            case default:
                print("Invalid choice!")

menu()