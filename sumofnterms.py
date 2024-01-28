#Using a for loop
sum = 0
print("Enter the Value of n: ")
n = int(input())
print("Enter " + str(n) + " Numbers: ")
for i in range(n):
    num = int(input())
    sum = sum+num
print("Sum of " + str(n) + " Numbers = " + str(sum))

#Using a while loop
sum = 0
i=0
print(end="Enter the Value of n: ")
n = int(input())
print(end="Enter " + str(n) + " Numbers: ")
while i<n:
    num = int(input())
    sum = sum+num
    i = i+1
print("\nSum of " + str(n) + " Numbers = " + str(sum))

#using a list
num = []
sum = 0
print(end="Enter the Value of n: ")
n = int(input())
print(end="Enter " + str(n) + " Numbers: ")
for i in range(n):
    num.insert(i, int(input()))
for i in range(n):
    sum = sum+num[i]
print("\nSum of " + str(n) + " Numbers = " + str(sum))
