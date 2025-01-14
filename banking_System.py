import random
import re
from datetime import datetime
import mysql.connector as my
con = my.connect(host = "localhost",port="3306", user="root",password = "user_password",database="banking_system")
cur = con.cursor()
login_status=False
status="active"
user_id=""
out1="select user_name,password from login"
cur.execute(out1)
o1=cur.fetchall()
ids=[]
uipd={}
usacc={}
for i in range(len(o1)):
    ids.append(o1[i][0])
    uipd[o1[i][0]]=o1[i][1]
account_no=[]
out2="select account_number,user_name from users"
cur.execute(out2)
o2=cur.fetchall()
for i in range(len(o2)):
   
    usacc[o2[i][1]]=o2[i][0]
    account_no.append(o2[i][0])


balance=0
email_id=[]

# This function is for registering new user
def register():
    global balance
    val1=[]
    val2=[]
    print("\n----Welcome To Registration Process----")
    name=input("Enter your name: ").lower()
    val1.append(name)
    n2=False
    while n2!=True:
        account=random.randint(1000000000,9999999999)
        if account in account_no:
            n2=False
        else:
            val1.append(account)
            val2.append(account)
            n2=True
           
    dob=input("Enter the dob in format(YYYY-MM-DD): ")
    val1.append(dob)
    city=input("Enter your city: ")
    val1.append(city)
    
    uname=input("Create a user name for your banking system: ")
    val1.append(uname)
    val2.append(uname)
    
    n4=False
    while n4!=True:
        print("Create a strong password\nIt should contain a upper case letter,a special character and digit")
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
            val1.append(password)
            val2.append(password)
            n4=True
        
    n=False
    while n!=True:
        balance=int(input("Enter the deposited amount: "))
        if balance>=2000:
            val1.append(balance)
            n=True
        else:
            print("minimum amount should be 2000")
    n1=False
    while n1!=True:
        contact=input("\nEnter your contact number: ")
        if len(contact)==10 and contact.isdigit()==True:
            val1.append(contact)
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
            val1.append(email)
            n3=True
        else:
            print("Enter a valid email ")
            n3=False


    address=input("\nEnter your address: ")

    val1.append(address)
    # print("For activating the account enter 1 or activate")
    # sta=input("Enter the status of your account:").lower()
    # if sta=="1" or sta=="activate":
    #     status="Active"
    # else:
    #     status="Not Active"
    sql1="insert into users (name,account_number,dob,city,user_name,password,balance,contact,email,address) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql1,val1)
    sql2="insert into login (account_number,user_name,password) value(%s,%s,%s)"
    cur.execute(sql2,val2)


    


# This function is for crediting  facility provided to user 
def credit():
    global balance
    global usacc
    n6=False
    while n6!=True:
        add=int(input("Enter the amount you want to credit in your account:  "))
        
        if add<0:
            n6=False
        else:
            out3="select balance from users where user_name=%s"
            cur.execute(out3,(user_id,))
            balance=cur.fetchone()
            # print(balance)
            new_balance=balance[0]+add
            out4="UPDATE users SET balance = %s WHERE user_name = %s"
            cur.execute(out4, (new_balance, user_id))  
            con.commit()
            current_date = datetime.now()
            today= current_date.strftime("%Y-%m-%d")
            o2="insert into transactions (account_number,transaction_type,amount,transaction_date) value(%s,%s,%s.%s)"
            cur.execute(o2,(usacc[user_id],"credit",add,today))
            con.commit()
            
            n6=True
    
    
# This function is for withdrawing facility provided to user
def debit():
    global balance
    n5=False
    while n5!=True:
        out3="select balance from users where user_name=%s"
        cur.execute(out3,(user_id,))
        balance=cur.fetchone()
        sub=int(input("Enter the amount you want to debit from your account:  "))
        if sub>balance[0]:
            n5=False
        else:
            new_balance=balance[0]-sub
            out4="UPDATE users SET balance = %s WHERE user_name = %s"
            cur.execute(out4, (new_balance, user_id))  
            con.commit()
            current_date = datetime.now()
            today= current_date.strftime("%Y-%m-%d")
            o2="insert into transactions (account_number,transaction_type,amount,transaction_date) value(%s,%s,%s.%s)"
            cur.execute(o2,(usacc[user_id],"debit",sub,today))
            con.commit()
            n5=True

# This function is for printing the available balance of the user account
def available_balance():
   global balance
   out3="select balance from users where user_name=%s"
   cur.execute(out3,(user_id,))
   balance=cur.fetchone()
   print("The available balance=",balance[0])

# This function is for changing password of the  user
def change_password():
    # out1="select user_name,password from login"
    # cur.execute(out1)
    # o1=cur.fetchall()
    global login_status
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
            out4="UPDATE users SET password = %s WHERE user_name = %s"
            cur.execute(out4, (password, user_id))  
            con.commit()
            out6="UPDATE login SET password = %s WHERE user_name = %s"
            cur.execute(out6, (password, user_id))  
            con.commit()
            con.close()
            print("Password is changed successfully please end program ")
            login_status=False
            n4=True

    
# This show function will print all information of the logined user
def show_profile():
    print("Show profile")
    out7="select * from users where user_name=%s"
    cur.execute(out7,(user_id,))
    info=cur.fetchone()
    name,account,dob,city,user_name,password,balance,contact,email,address,status=info
    print("Name: ",name)
    print("User Name: ",user_name)
    print("Account Number: ",account)
    print("DOB: ",dob)
    print("City: ",city)
    print("Balance: ",balance)
    print("Contact: ",contact)
    print("Email: ",email)
    print("Address: ",address)
    print("Account status: ",status)
    print("\n")



    
def transactions():
    print("transactions")
    o3="select * from transactions where account_number=%s"
    cur.execute(o3,(usacc[user_id],))
    o8=cur.fetchall()
    print(o8)

    
def transfer():
    p1=input("Enter the account number in which you want to transfer: ")
    if p1 in account_no:
        add=int(input("Enter the amount you want to transfer: "))
        out3="select balance from users where account_number=%s"
        cur.execute(out3,(p1,))
        balance=cur.fetchone()
        # print(balance)
        new_balance=balance[0]+add
        out4="UPDATE users SET balance = %s WHERE account_number = %s"
        cur.execute(out4, (new_balance, user_id))  
        con.commit()
        out3="select balance from users where user_name=%s"
        cur.execute(out3,(user_id,))
        balance=cur.fetchone()
        # print(balance)
        new_balance=balance[0]-add
        out4="UPDATE users SET balance = %s WHERE user_name = %s"
        cur.execute(out4, (new_balance, user_id))  
        con.commit()
        

# This function is for deactivating the account
def deactivate():
    global status
    print("Do you want to deactvate the account\n if yes the enter Y \n Else N")
    stat=input("Enter your Choice: ").upper()
    if stat=="Y":
        status="not active"
        out8="UPDATE users SET status = %s WHERE user_name = %s"
        cur.execute(out8, (status, user_id))  
        con.commit()
        print(f"User ID {user_id} is deactivated")
    else:
       status= "active"
       out9="UPDATE users SET status = %s WHERE user_name = %s"
       cur.execute(out9, (status, user_id))  
       con.commit()

def update_profile():
    print("update profile")
    print("Enter your choice of update:\n 1.name,2.dob,3.contact,4.city,5.address")
    update=input("Enter what you want to update: ").lower()
    if update==1 or update=="name":
        inp=input("Enter your updated name:")
        out9="UPDATE users SET name = %s WHERE user_name = %s"
        cur.execute(out9, (inp, user_id))  
        con.commit()
    elif update==2 or update=="dob":
        inp=input("Enter your updated dob(YYYY-MM-DD):")
        out9="UPDATE users SET dob = %s WHERE user_name = %s"
        cur.execute(out9, (inp, user_id))  
        con.commit()
    elif update==3 or update=="contact":
       
        n1=False
        while n1!=True:
            contact=input("\nEnter your contact number: ")
            if len(contact)==10 and contact.isdigit()==True:
                out9="UPDATE users SET contact = %s WHERE user_name = %s"
                cur.execute(out9, (contact, user_id))  
                con.commit()
                n1=True
            else:
                print("Enter a valid phone number\n")
    
    elif update==4 or update=="city":
        inp=input("Enter your updated city:")
        out9="UPDATE users SET city = %s WHERE user_name = %s"
        cur.execute(out9, (inp, user_id))  
        con.commit()
    elif update==5 or update=="address":
        inp=input("Enter your updated address:")
        out9="UPDATE users SET address= %s WHERE user_name = %s"
        cur.execute(out9, (inp, user_id))  
        con.commit()
    
            




        

# This function is for facility provided to user
def facility():
    global login_status
    global status
    login_status=True
    out10="select status from users where user_name=%s"
    cur.execute(out10,(user_id,))
    st=cur.fetchone()
    status=st[0]
   

    if status=="active":
        while login_status==True :   
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
    else:
        print("Account is not active do you want to activate account")
        print("IF yes the enter Y\n else N")
        choice=input("Enter your choice:").upper()
        if choice=="Y":
            status= "active"
            out9="UPDATE users SET status = %s WHERE user_name = %s"
            cur.execute(out9, (status, user_id))  
            con.commit()
            print("please logout and end program")
            login_status=False
    
# This is login function
def login():
   global ids
   global user_id
   global login_status
   global status
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
                status="active"

                 
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
    # global ids
    # global user_id
    global login_status
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
con.commit()
con.close()
# print(balance)
# print(user_id)
