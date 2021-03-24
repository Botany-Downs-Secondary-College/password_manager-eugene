#password_manager.py
#Did you write my code Anson and Alex - Eugene
# Yes we did - Alex and Anson
print("Hi, welcome to Eugene's password programme. You must be 13 or over to qualify. ")

password_list = []
new_user = []



#Functions 

def age():
  age = int(float(input("What is your age: ")))
  if age < 13:
    print("You do not qualify")
  elif age >= 13:
      print("You qualify and may proceed.")
      
      

age()

def new_user():

  
    new_user = input("Enter a username to create a user for a new account: ")
    x = len(new_user)
    print(x)
    if x >= 5:
      print("Amount of letters in username qualify")
    if x <5:
      short = print("Username is too short must contain 5 or more letters")

      print(short)
    
    
    
new_user()

def password():
  new_password = input("Please enter a password (must be 8 or higher): ")
  y = len(new_password)
  print(y,"is the amount of letters in your pass")
  if y < 8:
    print("password is too short")

  elif y >= 8:
    print("password length qualify")

  repeat = input("re-enter a new pass? yes or no: ")
  if repeat == "yes":
    password()
  else:
      print("Goodbye")


password()

#YOU got the rest EUGENE if you reading this - Alex, Anson






