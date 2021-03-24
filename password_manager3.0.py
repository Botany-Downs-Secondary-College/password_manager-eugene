#password_manager.py
#Did you write my code Anson and Alex - Eugene
# Yes we did - Alex and Anson
print("Hi, welcome to Eugene's password programme. You must be 10 or over to qualify. ")

password_list = []
user_list = []



#Functions 

def age():
  age = int(float(input("What is your age: ")))
  if age < 10:
    print("You do not qualify")
  elif age >= 10:
      print("You qualify and may proceed.")
age() 
def new_user():
  while True:

    new_user = input("Enter a username to create a user for a new account: ")
    x = len(new_user)
    print(x)
    if x >= 5:
      print("Amount of letters in username qualify")
      user_list.append(new_user)
      break
    else:
      print("Username is too short must contain 5 or more letters")

def password():
    while True:
        new_password = input("Please enter a password (must be 8 or higher): ")
        y = len(new_password)
        print(y, "is the amount of letters in your pass")
        if y >= 8:
            print("password length qualify")
            password_list.append(new_password)
            break
        else:
            print("Password is too short try again.")   


while True:
  option = input("1:New User 2:View User List 3: View Password: ")
  if option == "1":
      new_user()
      password()
      
  elif option == "2":
      print(user_list)
  elif option == "3":
      print(password_list)
      break
  else:
    print("error, enter a number again.")









  

#YOU got the rest EUGENE if you reading this - Alex, Anson






