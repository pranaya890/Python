n=int(input("Enter a number:"))
prime=True
for i in range (2,int(n/2)+1):
    if n%i==0:
        prime=False
        break

print(prime)
