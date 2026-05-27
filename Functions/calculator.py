def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def pro(a,b):
    return a*b

def div(a,b):
    return a/b


a= int(input("Enter a number"))
b=int(input("Enter another number:"))

print("What do you want to do?")
print("1.Add \n 2.Subtract \n 3.Multiply \n 4. Divide\n press other key to exit")
ch = int(input("Enter your choice"))

while ch!=5 and ch <6:
    if ch==1:
        print(add(a,b))
        ch = int(input("Enter your choice"))
    elif ch==2:
        print(sub(a,b))
        ch = int(input("Enter your choice"))
    elif ch==3:
        print(pro(a,b))
        ch = int(input("Enter your choice"))
    elif ch==4:
        print(div(a,b))
        ch = int(input("Enter your choice"))
    else:
        break

