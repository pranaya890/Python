#Take 3 numbers as input and print the largest one.
a=int(input("Enter a Number"))
b=int(input("Enter a Number"))
c=int(input("Enter a Number"))

if a>b and a>c:
    print(a,"is the greatest number")
elif b>c:
    print(b ,"is greatest number")
else:
    print(c,"is the greatest")
    