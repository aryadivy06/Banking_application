import mysql.connector as my
con = my.connect(host = "localhost",port="3306", user="root",password = "user_password",database="banking_system")
cur = con.cursor()

##This is to create a data base banking_system Which will store the tables
# sql = "create database banking_system;"
# cur.execute(sql)

#This is to create table which stores the user information

sql1="""CREATE TABLE users (
    name VARCHAR(100),
    account_number VARCHAR(10) PRIMARY KEY,
    dob DATE,
    city VARCHAR(50),
    password VARCHAR(50),
    balance DECIMAL(10, 2),
    contact VARCHAR(10),
    email VARCHAR(100),
    address TEXT,
    status VARCHAR(10) DEFAULT 'active'
);"""
cur.execute(sql1)

#This is to create table which stores the login user  information

sql2="""CREATE TABLE login (
    account_number VARCHAR(10) PRIMARY KEY,
    password VARCHAR(50)
);"""
cur.execute(sql2)

#This is to create table which stores the transaction information

sql3="""CREATE TABLE transactions (
    account_number VARCHAR(10),
    transaction_type VARCHAR(10),
    amount DECIMAL(10, 2),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""
cur.execute(sql3)


con.commit()
con.close()