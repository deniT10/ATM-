class Account():
    hasLogedIn = False
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        while(True):
            try:
                deposite_amount = int(input("\nYour currently have "+str(self.balance)+ " $\nHow much money do you want to deposite?\n"))
                self.balance = self.balance + deposite_amount
                print(str(deposite_amount)+"$ have been deposite to your account.\nThe current amount is "+str(self.balance)+"$")
                break
            except Exception as ex:
                print("please input a valid number")
                deposite_amount = 0
        

    def withdraw(self):
        while(True):
            try:
                withdraw_amount = int(input("\nYour currently have "+str(self.balance)+ " $\nHow much money do you want to withdraw?\n"))
                if withdraw_amount <= self.balance:
                    self.balance = self.balance - withdraw_amount
                    print(str(withdraw_amount)+ "$ have been withdrawn.\nThe current amount is "+str(self.balance)+"$")
                    break
                else:
                    print("You dont have enough money to perform this withdrawel")
            except:
                print("\nPlease input a valid number")
    
    def login(self):
        psw = input("Put in the password: ")
        if( psw == "123456"):
            self.start()

    def GetBalance(self):
        print("Balance is "+str(self.balance)+"$")

    def start(self):
        while(True):
            action = input("\nPress 1 to check the balance\nPress 2 to withdraw money\nPress 3 to deposite\nPress 4 to log out\n")
            if(action ==  "1"):
                self.GetBalance()
            elif(action == "2"):
                self.withdraw()
            elif(action == "3"):
                self.deposit()
            elif(action=="4"):
                print("You have been logged out")
                break
            else:
                print("Please input a valid option")

account = Account("Deni", 1500)
account.login()
