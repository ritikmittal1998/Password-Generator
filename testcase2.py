import random 
import pyperclip  as pc

password = "" 
def calculate_password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    global password 

    length = int(input("Enter Lenght :"))

    print("Enter Strenght Of password(low, medium, strong)")

    strength = input("Enter strenght :")

    #If strenght is low
    if strength == "low":
        for i in range(0, length): 
            password = password + random.choice(lower) 
        print(password)
        #pc.copy(password) 

    #If strenght is Medium
    elif strength == 'medium':
        for i in range(0, length): 
            password = password + random.choice(upper) 
        print(password)
       # pc.copy(password)  

    #If strenght is Strong
    elif strength== 'strong':
        for i in range(0, length): 
            password = password + random.choice(digits) 
        print(password) 
        #pc.copy(password) 
    else: 
        print("Please choose an option")

def copy_pass():
   
    print("Do you want to copy Your Password: YES/NO")
    replica = input()
    if replica.casefold() == "yes":
        pc.copy(password)
        
    
    

# Main function calling
calculate_password()
copy_pass()






