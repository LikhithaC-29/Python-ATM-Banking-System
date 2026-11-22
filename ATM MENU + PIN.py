pin = 1234
balance = 15000

def checkbalance():
    print("the balance is",balance)
    
def deposit():
    global balance
    print("enter the amount to deposit")
    dep=int(input())
    if (dep<=0):
        print("invalid amount")
    else:
        print(dep,"deposited succesfully")
    
        print("balance",balance+dep)
        balance += dep

def withdraw():
    global balance 
    print("enter the amount to withdraw")
    wd=int(input())
    if(wd<=0):
        print("invalid withdrawal amount")
    elif (wd > balance):
        print("amount cannot be withdrawn since it is greater than balance")
    else:
        print(wd,"withdrawn succesfully")
        print("balance",balance-wd)
        balance -= wd

def exit_atm():
    print("thank you!")
    
failed_attempt = 0
while True:
    print("enter the atm pin")
    pinn = int(input())
    if pinn!= pin:
        print("wrong pin")
        failed_attempt = failed_attempt + 1
        print("you have", 3-failed_attempt,"attempts")
        if failed_attempt == 3:
            print ("account is locked")
            break;
    else:
        while True:
            print('''\n1.check balance\n2.deposit\n3.withdraw\n4.exit\n''')
            print("Enter your choice : ")
            choice=int(input())
            if choice == 1:
                checkbalance()
            
            elif choice == 2:
                deposit()
            
            elif choice == 3:
                withdraw()
            
            elif choice == 4:
                exit_atm()
                break;
            else:
                print("invalid choice")
        break
           
       