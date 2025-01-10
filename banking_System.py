import random
import re
login_status=False
user_id=""
ids=["d06","s06"]
# ids=[]
marks=0
account_no=[]
balance=0
email_id=[]

uipd={"d06":"12","s06":"12"}
def register():
    print("\n----Welcome To Registration Process----")
    name=input("Enter your name: ").lower()
    n2=False
    while n2!=True:
        account=random.randint(1000000000,9999999999)
        if account in account_no:
            n2=False
        else:
            account_no.append(account)
            n2=True
    dob=input("Enter the dob in format(DD-MM-YYYY): ")
    city=input("Enter your city: ")
    
    uname=input("Create a user name for your banking system: ")
    
    n4=False
    while n4!=True:
        print("Create a strong password\nIt should contain a upper case letter,,a special character and digit")
        password=input("Create password: ")
        if not re.search(r"[A-Z]", password):
            print("Password must contain at least one uppercase letter.")
            n4=False
    
    
        elif not re.search(r"[a-z]", password):
            print("Password must contain at least one lowercase letter.")
            n4=False
        
        # Check for at least one digit
        elif not re.search(r"[0-9]", password):
            print("Password must contain at least one digit.")
            n4=False
        
        # Check for at least one special character
        elif not re.search(r"[!@#$%^&*_()\-+]", password):
            print("Password must contain at least one special character (!@#$%^&*()-+).")
            n4=False
        else:
            n4=True
        
    n=False
    while n!=True:
        balance=int(input("Enter the deposited amount: "))
        if balance>=2000:
            n=True
        else:
            print("minimum amount should be 2000")
    n1=False
    while n1!=True:
        contact=input("\nEnter your contact number: ")
        if len(contact)==10 and contact.isdigit()==True:
            n1=True
        else:
            print("Enter a valid phone number\n")
    
    n3=False
    while n3!=True:
        email=input("\nEnter your email ID: ").lower()
        if email in email_id  :
            print("This email is already registered enter a new email id")
            n3=False
        elif email=="@gmail.com":
            n3=False
        elif "@gmail.com" in email:
            n3=True
        else:
            print("Enter a valid email ")
            n3=False


    address=input("\nEnter your address: ")

   
def credit():
    print("credit")
    add=int(input("Enter the amount you want to credit in your account:  "))
    balance=balance+add
    print("The new balance=",balance)
def debit():
    print("debit")
    n5=False
    while n5!=True:
        sub=int(input("Enter the amount you want to debit from your account:  "))
        if sub>balance:
            n5=False
        else:
            balance=balance-sum
            print("The new balance=",balance)
            n5=True
def available_balance():
   print("The available balance=",balance)

def change_password():
    print("change password")
    n4=False
    while n4!=True:
        print("Create a strong password\nIt should contain a upper case letter,,a special character and digit")
        password=input("Create a new  password: ")
        if not re.search(r"[A-Z]", password):
            print("Password must contain at least one uppercase letter.")
            n4=False
    
    
        elif not re.search(r"[a-z]", password):
            print("Password must contain at least one lowercase letter.")
            n4=False
        
        # Check for at least one digit
        elif not re.search(r"[0-9]", password):
            print("Password must contain at least one digit.")
            n4=False
        
        # Check for at least one special character
        elif not re.search(r"[!@#$%^&*_()\-+]", password):
            print("Password must contain at least one special character (!@#$%^&*()-+).")
            n4=False
        else:
            n4=True
    print("Password is changed successfully")

def show_profile():
    print("Show profile")
    
def transactions():
    print("transactions")

    
def transfer():
    print("transfer")
def deactivate():
    print("deactivate")

def update_profile():
    print("update profile")

        


def facility():
    login_status=True
    while login_status==True:   
        print("Choose the facility you want to use form the below\n")
        print("\n1.Transactions\n2.Credit amount\n3.Debit amount\n4.Transfer amount\n5.Deactivate account\n6.Available balance\n7.Show profile\n8.Update profile\n9.Change password\n10.Exit")
        fac=input("Enter the facility you want:").lower()
        if fac=="1" or fac=="transactions":
            transactions()
        elif fac=="2" or fac=="credit" or fac=="credit amount":
            credit()
        elif fac=="3" or fac=="debit" or fac=="debit amount":
            debit()
        elif fac=="4" or fac=="transfer" or fac=="transfer amount":
            transfer()
        elif fac=="5" or fac=="deactivate" or fac=="deactivate account":
            deactivate()
        elif fac=="6" or fac=="available balance" or fac=="balance":
            available_balance()
        elif fac=="7" or fac=="show profile" or fac=="profile":
            show_profile()
        elif fac=="8" or fac=="update profile":
            update_profile()
        elif fac=="9" or fac=="change password":
            change_password()
        elif fac=="10" or fac=="exit":
            print("Loging out")
            login_status=False
        else:
            print("Invalid Choice")

    
# This is login function
def login():
   print("Enter your details")
   m=False
   while m!=True:
     user_id=input("\nEnter your user id: ")
     if user_id in ids:
         
         k=False
         while k!=True:
             p=input("Enter your password: ")
             if uipd[user_id]==p:
                login_status=True
                 
                m=True
                k=True
                facility()
             else:
                 print("Invalid password")
                #  p=input("Enter your password: ")
                #  m=False
                #  k=False
     else:
         print("\nUser not exist go to register")
         m=True
     
     



# This is main function
def main():
    print("\n----------Welcome To Banking Application----------\n")
   
    l=False
    while l!=True:
        if login_status==True:
            facility()
            

        else:
            print("Choose option from below\n")
            print("1.Register or Create account \n2.Login\n3.Logout\n")
            choice=input("Enter your choice: ").lower()
            if choice=="1" or choice=="register" or choice=="create account":
               
                register()
            elif choice=="2" or choice=="login":
                login()
            elif choice=="3" or choice=="logout" or choice=="exit":
                print("Exiting Application")
                l=True
            else:
                 print("Invalid choice")
                 l=False
    
            

main()