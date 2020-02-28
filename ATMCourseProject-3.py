"""
*******************************************************************************
* Program:  ATMCourseProject.py
* Author: Kamal Basnet
* Course: MI 261 Fall
*
* Description: This program is an income tax calculator. 
*
* Edit History / Change Log
* DATE                  CHANGE DESCRIPTION
* ----------------------------------------
* 2018-09-21            Initial program
* 2018-10-06            Deposit Function
* 2018-10-15            Print Function
*******************************************************************************
"""
#Below are the executables


#variables
accountNumber = '123456'
pin = '999'
startCheckingAcctBalance = 500
savingsAccountBalance1 = 1500
savingsAccountBalance2 = 5000
depositCheckingAcctTotal = 0
depositSavingsAcct1Total = 0
depositSavingsAcct2Total = 0
depositTotal = 0
withdrawCheckingAcctTotal = 0
withdrawSavingsAcct1Total = 0
withdrawSavingsAcct2Total = 0
withdrawTotal = 0
remainingBalanceCh= startCheckingAcctBalance
remainingBalanceS1 = savingsAccountBalance1
remainingBalanceS2= savingsAccountBalance2

exitCode = 'exit'


print('Welcome to Python ATM Machine.\n')
 
def main():
#Main infrastuture of the ATM
    incorrectPin = True
    while incorrectPin:
        userAccountNumber = input('Please Enter your Account Number:')
        if userAccountNumber == exitCode:
            incorrectPin = False
        else:
            userPin = input('Please Enter Your Account Pin:')
            
            if  userAccountNumber == accountNumber and userPin == pin:
                print ('Your Login Credentials are Correct')
                option = options()
                while option != 4:
                    if option == 1: #displays balance information
                        print('Your checking account balance is $', remainingBalanceCh,
                            '\nYour First savings account balance is $',remainingBalanceS1,
                            '\nYour Second savings account balance is $',remainingBalanceS2)
                        
                    elif option == 2:
                        depositFunction()  #calls deposit function
                    elif option == 3:
                        withdrawFunction()
                    
                    else:
                        print('Please Reenter your options')
                    option = options()
                goodbye()
                incorrectPin = False
            else:
                print("Sorry, you have entered wrong credentials, try again!")
            
            
               
    
def options():  #allows users to choose which account
    invalidOption = True
    while invalidOption == True:
        try:
            #prompt allow user to choose 
            option = int(input('''
            
            Please choose an option from the following:  
            \t 1 - Balance
            \t 2 - Deposit
            \t 3 - Withdraw
            \t 4 - Exit  \n
            \t Enter an option: '''))
            
            if option in (1,2,3,4): # proceeds if 1,2,3,4
                invalidOption = False
            else: 
                invalidOption = True
        except:#any option other than 1,2,3,4
            print('You Entered A Wrong Option. Please select one of the options')
            
        return option
    
def goodbye():
    
    
    anothertras = 'yes'    
    anothertras = input('\nWould you like another transcation? Yes or No ?: ')
    if anothertras == 'yes':
        print('\nPlease Reenter your Credentials to proceed \n')
        main()
        
     
    else:
        print('Thank you for using ATM Today \n')
        printFunction()
     
    
    
        
                
def depositFunction(): #function for the deposit
    global startCheckingAcctBalance
    global remainingBalanceCh
    global savingsAccountBalance1
    global remainingBalanceS1
    global savingsAccountBalance2
    global remainingBalanceS2
    global depositCheckingAcctTotal
    global depositSavingsAcct1Total
    global depositSavingsAcct2Total
    global depositTotal
    global withdrawCheckingAcctTotal
    global withdrawSavingsAcct1Total
    global withdrawSavingsAcct2Total
    global withdrawTotal
    
    invalidOption = True
    while invalidOption: #allows users to choose which acccount they want to deposit on.
            depositChoice = int(input(''' 
            Which account would you like to deposit into?:
            \t 1 - Checking Account
            \t 2 - Savings Account 1
            \t 3 - Savings Account 2
            \n \t Enter a number according to the option: '''))


            if depositChoice > 0 and depositChoice < 4:
                invalidOption = False
                
            else:
                invalidOption = True
                print('You Entered A Wrong Option. Please select one of the options')
            if depositChoice == 1:
                depositChecking = input("Enter deposit amount: ")
                if depositChecking.isnumeric(): #verfies the input
                    depositChecking = int(depositChecking)
                    if depositChecking >0 and depositChecking<=1000:
                        remainingBalanceCh += depositChecking
                        depositCheckingAcctTotal += depositChecking
                        print("New Balance is: $ ", remainingBalanceCh)
                    else:
                        print("Please enter any amount between $1 and $1000")
                        
    
            elif depositChoice == 2:
                depositSavingsA1 = input("Enter deposit amount: ")
                if depositSavingsA1.isnumeric(): #verfies the input
                    depositSavingsA1 = int(depositSavingsA1)
                    if depositSavingsA1 >0 and depositSavingsA1<=1000:
                        remainingBalanceS1 += depositSavingsA1
                        depositSavingsAcct1Total += depositSavingsA1
                        print("New Balance is: $ ", remainingBalanceS1)
                    else:
                        print("Please enter any amount between $1 and $1000")
                        
            elif depositChoice == 3:
                depositSavingsA2 = input("Enter deposit amount: ")
                if depositSavingsA2.isnumeric(): #verfies the input
                    depositSavingsA2 = int(depositSavingsA2)
                    if depositSavingsA2 >0 and depositSavingsA2<=1000:
                        remainingBalanceS2 += depositSavingsA2
                        depositSavingsAcct2Total += depositSavingsA2
                        print("New Balance is: $ ", remainingBalanceS2)
                    else:
                        print("Please enter any amount between $1 and $1000")
                        
            else:
                print('You Entered A Wrong Option. Please select one of the options')
                
            
    invalidOption = False                       
def withdrawFunction(): #function for the deposit
    global startCheckingAcctBalance
    global remainingBalanceCh
    global savingsAccountBalance1
    global remainingBalanceS1
    global savingsAccountBalance2
    global remainingBalanceS2
    global depositCheckingAcctTotal
    global depositSavingsAcct1Total
    global depositSavingsAcct2Total
    global depositTotal
    global withdrawCheckingAcctTotal
    global withdrawSavingsAcct1Total
    global withdrawSavingsAcct2Total
    global withdrawTotal
    
    invalidOption = True
    while invalidOption: #allows users to choose which acccount they want to withdraw on.
            withdrawChoice = int(input(''' 
            Which account would you like to deposit into?:
            \t 1 - Checking Account
            \t 2 - Savings Account 1
            \t 3 - Savings Account 2
            \n \t Enter a number according to the option: '''))


            if withdrawChoice > 0 and withdrawChoice < 4:
                invalidOption = False
                
            else:
                invalidOption = True
            # checking account withdrawal
            if withdrawChoice == 1:
                if withdrawCheckingAcctTotal < 300 and withdrawTotal <750:
                    print('Current Checking balance:$',remainingBalanceCh) 
                    withdrawalChecking = input( 'Enter Deposit Amount in denomination of $20:')
                
                    if withdrawalChecking.isnumeric(): #verfies the input
                        withdrawalChecking = int(withdrawalChecking)
                        if withdrawalChecking ==20 or 40 or 60 or 80 or 100:
                            if((withdrawalChecking + withdrawCheckingAcctTotal) <= 300 and (withdrawalChecking + withdrawTotal) <= 750):
                                remainingBalanceCh = (remainingBalanceCh-withdrawalChecking)

                                withdrawCheckingAcctTotal += withdrawalChecking
                        
                                print("New Balance is: $ ", remainingBalanceCh)
                            else:
                                print("Withdrawal Limit has reached. Please enter the amount again")
                        else:
                            print("Please enter amount in denominations of $20, $40, $60, $80, $100")
                    else:
                        print("Please enter amount in denominations of $20, $40, $60, $80, $100")
                else:
                    print("Withdrawal Limit has reached.")
                    
                        
    
            elif withdrawChoice == 2:
                if withdrawSavingsAcct1Total < 300 and withdrawTotal <750:
                    print('Current Checking balance:$',remainingBalanceS1) 
                    withdrawalSavings1 = input( 'Enter Deposit Amount in denomination of $20:')
                
                    if withdrawalSavings1.isnumeric(): #verfies the input
                        withdrawalSavings1 = int(withdrawalSavings1)
                        if withdrawalSavings1 ==20 or 40 or 60 or 80 or 100:
                            if((withdrawalSavings1 + withdrawSavingsAcct1Total) <= 300 and (withdrawalSavings1 + withdrawTotal) <= 750):
                                remainingBalanceS1 = (remainingBalanceS1-withdrawalSavings1)

                                withdrawSavingsAcct1Total += withdrawalSavings1
                        
                                print("New Balance is: $ ", remainingBalanceS1)
                            else:
                                print("Withdrawal Limit has reached. Please enter the amount again")
                        else:
                            print("Please enter amount in denominations of $20, $40, $60, $80, $100")
                    else:
                        print("Please enter amount in denominations of $20, $40, $60, $80, $100")
                else:
                    print("Withdrawal Limit has reached.")
            elif withdrawChoice == 3:
                if withdrawSavingsAcct2Total < 300 and withdrawTotal <750:
                    print('Current Checking balance:$',remainingBalanceS2) 
                    withdrawalSavings2 = input( 'Enter Deposit Amount in denomination of $20:')
                
                    if withdrawalSavings2.isnumeric(): #verfies the input
                        withdrawalSavings2 = int(withdrawalSavings2)
                        if withdrawalSavings2 ==20 or 40 or 60 or 80 or 100:
                            if((withdrawalSavings2 + withdrawSavingsAcct2Total) <= 300 and (withdrawalSavings2 + withdrawTotal) <= 750):
                                remainingBalanceS2 = (remainingBalanceS2-withdrawalSavings2)

                                withdrawSavingsAcct2Total += withdrawalSavings2
                        
                                print("New Balance is: $ ", remainingBalanceS2)
                            else:
                                print("Withdrawal Limit has reached. Please enter the amount again")
                        else:
                            print("Please enter amount in denominations of $20, $40, $60, $80, $100")
                    else:
                        print("Please enter amount in denominations of $20, $40, $60, $80, $100")
                else:
                    print("Withdrawal Limit has reached.")
                        
            else:
                print('You Entered A Wrong Option. Please select one of the options')
                
            
    invalidOption = False      
def printFunction():
    global startCheckingAcctBalance
    global remainingBalanceCh
    global savingsAccountBalance1
    global remainingBalanceS1
    global savingsAccountBalance2
    global remainingBalanceS2
    global depositCheckingAcctTotal
    global depositSavingsAcct1Total
    global depositSavingsAcct2Total
    global depositTotal
    global withdrawCheckingAcctTotal
    global withdrawSavingsAcct1Total
    global withdrawSavingsAcct2Total
    global withdrawTotal
    
    print("\nYour current Account Balance:")
    #checking account balance
    print("\nChecking Account")
    print("Your starting balance: ", startCheckingAcctBalance)
    print("Total deposits made: ", depositCheckingAcctTotal)
    print("Total withdrawals made: ", withdrawCheckingAcctTotal)
    print("Your new account balance is: ", remainingBalanceCh)
    
    
    #First Savings account balance
    print("\nFirst Savings Account")
    print("Your starting balance: ", savingsAccountBalance1)
    print("Total deposits made: ", depositSavingsAcct1Total)
    print("Total withdrawals made: ", withdrawSavingsAcct1Total)
    print("Your new account balance is: ", remainingBalanceS1)

    #Second Savings account balance
    print("\nSecond Savings Account")
    print("Your starting balance: ", savingsAccountBalance2)
    print("Total deposits made: ", depositSavingsAcct2Total)
    print("Total withdrawals made: ", withdrawSavingsAcct2Total)
    print("Your new account balance is: ", remainingBalanceS2)
    
















main()
#end of program
 
