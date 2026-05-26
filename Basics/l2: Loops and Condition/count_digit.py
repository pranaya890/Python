n=int(input("Enter a number:"))
count=0

while n>=10:
    count+=1
    n=n/10
count+=1
print(f"The number of digits are: {count}")

