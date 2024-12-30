login_status=False
user_id=""
ids=["d06","s06"]
marks=0
uipd={"d06":"12","s06":"12"}
def register():
    print("\n----Welcome To Registration Process----")
    name=input("Enter your name: ").lower()
    dob=input("Enter your date of birth:")

def show_profile():
    print("Show profile")
def transactions():
    print("transactions")
def credit():
    print("credit")
def debit():
    print("debit")
def transfer():
    print("transfer")
def deactivate():
    print("deactivate")
def available_balance():
   print("balance")
def update_profile():
    print("update profile")
def change_password():
    print("change password")

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
         p=input("Enter your password: ")
         k=False
         while k!=True:
             if uipd[user_id]==p:
                login_status=True
                 
                m=True
                k=True
                facility()
             else:
                 p=input("Enter your password: ")
                 m=False
                 k=False
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