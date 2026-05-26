print("Welcome to our Bank")
bal=0

print("Menu \n 1. Check Balance \n 2. Deposit \n 3.Withdraw  \n 4.Exit")
n=int(input("Enter your choice:"))

while n!=4:
    if n==1:
        print(f"The balance={bal}")
        n=int(input("Enter your choice:"))
    elif n==2:
        dep=int(input("Enter the amount to Deposit:"))
        bal+=dep
        print(f"The new balance={bal}")
        n=int(input("Enter your choice:"))
    else:
        wit=int(input("Enter the amount to withdraw:"))
        if wit>bal:
            print("Insufficient Balance")
            n=int(input("Enter your choice:"))
        else:
            bal-=wit
            print("Successful")
            n=int(input("Enter your choice:"))


print("Thank you for Banking process!")


    
