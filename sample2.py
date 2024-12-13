class Bank:
    accbal = 30000

    def deposit(self):
        amount = int(input("Enter Depositing Amount: "))
        if amount < 100:
            print("Minimum deposit amount should be 100rs/-")
        elif amount % 100 != 0:
            print("Depositing amount should be multiples of 100")
        elif amount > 50000:
            print("Maximum deposit amount is 50K")
        else:
            self.accbal += amount
            print(amount, "credited in your bank account successfully!!")

    def withdraw(self):
        amount = int(input("Enter Withdrawal Amount: "))
        if amount < 100:
            print("Minimum withdrawal amount should be 100rs")
        elif amount % 100 != 0:
            print("Withdrawal amount should be multiples of 100")
        elif amount > 20000:
            print("Maximum withdrawal transaction limit is 20K")
        else:
            if self.accbal - amount < 500:
                print("Bank Account should maintain minimum balance of 500- \nYour current balance is", self.accbal)
            else:
                self.accbal -= amount
                print("The amount debited from your account is:", amount)

    def balEnquiry(self):
        print("\nYour Account Balance is: ", self.accbal)

    def display(self):
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Bal Enquiry')
        print('4. Exit')
        while True:
            op = int(input("Please enter an option: "))
            if op == 1:
                obj.deposit()
            elif op == 2:
                obj.withdraw()
            elif op == 3:
                obj.balEnquiry()
            elif op == 4:
                print("\nThank You for your support!")
                break
            else:
                print("Enter valid option (1-4)")

    def validate(self):
        count = 0
        while count < 3:
            pin = int(input("Enter PIN No: "))
            if pin == 1234:
                obj.display()
                break
            else:
                count += 1
                if count != 3:
                    print("Wrong PIN! Please try again")
                else:
                    print("Your Account is blocked!")


obj = Bank()
obj.validate()
