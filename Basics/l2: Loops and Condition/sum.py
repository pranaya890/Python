#Take n as input and print the sum from 1 to n.

n=int(input("Enter the number:"))
sum=0

for i in range (1,n+1):
    sum+=i

print(f"The sum of numbers from 1 to {n} is {sum}")


#method 2

sum1=(n*(n+1))/2
print(f"The sum of numbers from 1 to {n} is {sum1} using direct formula")