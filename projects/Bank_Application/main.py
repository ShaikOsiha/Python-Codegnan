
#creating table
#accounts_table={account:password}
#users_table={account:[amount,Name,email]}

accounts_table={1234:456,
                1235:457}

users_table={1234:[1000,'Osiha','shaikosiha52@gmail.com'],
             1235:[500,'Teepu','teepumohaseen123@gmail.com']}

#functions
#login function
def login(username:int,password:int):
    #checking the account number exist in accounts table or not
    if username in accounts_table:
        #checking the password
        if password==accounts_table[username]:
            print("Login successfull")
            return True
        else:
            print("Check with credentials")
            return False
    else:
        print("User Not Found")
        return False


#withdraw function definition
def withdraw(account:int,withdraw_amount:int):
    #checking account in users table
    if account in users_table:
        amount=users_table[account][0]
        #checking amount is suffient  or not
        if amount>=withdraw_amount:
            users_table[account][0]-=withdraw_amount
            print(f"{withdraw_amount} withdraw successfully and \
                  current balance is {users_table[account][0]}") #\ means continue or write in single line
        else:
            print("Insuffient amount in your account")
    else:
        print("User not found")

#deposit function
def deposite(account:int,deposite_amount:int):
    #checking account in users table
    if account in users_table:
        #validating amount
        if deposite_amount>0:
            users_table[account][0]+=deposite_amount
            print(f"{deposite_amount}deposite successfully  and current balance is:{users_table[account][0]}")
        else:
            print("Checking with your deposite amount")
    else:
        print("User not Found")

    
   

#transfer function definition
def transfer(sender:int,receiver:int,transfer_amount:int):
    if sender in users_table:
        if transfer_amount>0:
            amount= users_table[sender][0]
            #receiver  account is present in users table or not
            if receiver in users_table:
                #checking amount is sufficient or not
                if amount>=transfer_amount:
                    users_table[sender][0]-=transfer_amount
                    users_table[receiver][0]+=transfer_amount
                    print(f"{transfer_amount} Transfer successfull and \
                          current balance is:{users_table[sender][0]}")
                else:
                    print("InSuffient amount in your account")   
            else:
                print("Receiver account is not found")
        else:
            print("User is not found")



   


#ministatement function definition
def ministatement(account:int):
    print("Ministaement page development under processing")

# Balance Enquiry function definition
def balanceenquiry(account:int):
    if account in users_table:
        print(f"current balance is:{users_table[account][0]}")
    else:
        print("User not found")



#logout function definition
def logout():
    print("Logout successfully")
    exit()

#main
if __name__== "__main__":
    print("Welcome to the Codegnan Bank Application")
    username=int(input("Enter your account number:"))
    password=int(input("Enter your password:"))
    login_val=login(username=username,password=password) #login is function
    while login_val:
        operations=("1.withdraw\n",
                    "2.deposite\n",
                    "3.transfer\n",
                    "4.miniStatement\n",
                    "5.balanceenquiry\n",
                    "6.logout\n"
                      )
        print(*operations)
        choice=int(input("Select your operation:"))
        if choice==1:
            amount=int(input("Enter your withdraw amount"))
            withdraw(account=username,withdraw_amount=amount)

        elif choice==2:
            amount=int(input("Enter your deposite amount "))
            deposite(account=username,deposit_amount=amount)
        
        elif choice==3:
            amount=int(input("Enter recevier account number:"))
            amount=int(input("Enter transfer amount:"))
            transfer(sender=username,receiver=account,transfer_amount=amount)

        elif choice==4:
            ministatement(account=username)
        
        elif choice==5:
            balanceenquiry(account=username)
        
        elif choice==6:
            logout()

        else:
            print("select your operation between 1-6")

        
    
    
     
