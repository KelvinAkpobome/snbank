#importing modules
import os
from datetime import datetime
import random


#options for staff selection 
def selection():
    initialoption = input("Please select an option below to proceed.\n\t1 Login, Staff Only\n\t2 Exit\n\t> ")
        
    if initialoption == '1':
        un = input("Please enter Username here: ")
        pd = input("Please enter Password here: ")
#verify if login details match with predefined details 
        def passwordverify(un, pd, verify):
            for line in verify:
                if un in line and pd in line:
                #creates a session and saves in a .txt file
                    session = open("session.txt")
                    logindetails = str(datetime.now())
                    session.write(logindetails)
                    session.close()
#user login was successful
                    def successfullogin():
                        loginsuccess = input("Please select an option below \n\t1 Create new bank account\n\t2 Check Account details\n\t3 Logout\n\t> ")
                        if loginsuccess == '1':
                            #staff Creates bank account 
                            nameOfAccount = input("Please enter account name here: ")
                            balanceUponOpening = input("Please specify balance upon opening here: #")
                            accType = input("Please enter account type here: ")
                            accEmail = input("Please enter account e-mail here: ")

                            #generating a 10 digits account number for the customer.
                            global accNumber
                            accNumber = random.randrange(1000000000,10000000000)
                            customerdoc = open("customer.txt","w")
                            customerdoc.write("Account Name: %s Balance: %s Type: %s Email: %s Acc number: %d\n" % (nameOfAccount, balanceUponOpening, accType, accEmail, accNumber))
                            customerdoc.close()
                            print(f"The account number of the customer is {accNumber}\n")
                            successfullogin()
                        elif loginsuccess == '2':
                            #requesting for account number.
                            def loginsucces1():
                                checkAccount = input("Input your account number: ")
                                if checkAccount == str(accNumber):
                                    customerread = open("customer.txt","r")
                                    customerread = customerdoc.read()
                                    print(customerread)
                                    customerdoc.close()
                                    loginsucces1()
                                else:
                                    print("Invalid account number, Please try again.\n")
                                    loginsucces1()
                            loginsucces1()

                        #deleting the user session file and returning the user back to the staff login page.
                        elif loginsuccess == '3':
                            os.remove("session.txt")
                            selection()

                    successfullogin()


                else:
                    print("Incorrect login details, please try again.\n")
                    selection()
                    

    
        passwordverify(un, pd, open('staff.txt').readlines())
    #exiting program.
    elif initialoption == '2':
        exit(0)
    else:
        print("Please make a valid selection\n")
        passwordverify()


selection()