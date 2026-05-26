n=int(input("Enter the number:"))
org=n
m=n
sum=0
count=0

while m>0:
    m=m//10
    count+=1

m=n

while m>0:
    x=m%10
    sum=sum+x**count
    m=m//10

if sum==org:
    print("The number is armstrong number")
else:
    print("It is not")
