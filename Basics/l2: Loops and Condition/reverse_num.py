n=int(input("Enter a number:"))
rev=0
while n>=10:
    x=n%10
    rev=rev*10+x
    n=(n-x)/10    
rev=rev*10+n

print(int(rev))


