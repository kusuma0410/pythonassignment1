#   /02/24   monday

#write a functiom given number is even or odd 
#num = int (input ("given number is odd or even: "))
#if (num % 2) == 0:
 #   print ("The number is even")
#else:
 #   print ("The number is odd")

#num=32
#if(num%2)==0:
 #   print(num,"num is even")
#else:
 #  print(num,"num is odd")

#write a func which contains some number as arg and print square of that numbers
#n=int(input())
#def square_num():
   # a = n**2
  #  my_result = a
 #   return my_result
#print(square_num())

#num = 2
#square = num ** 2
#print(square)

#num = 5
#square = num ** 2
#print(square)

#write a function to find factorial of given numbers
#def factorial(n):
 #   return 1 if (n==1 or n==0) else n * factorial(n - 1) 
#num = 5
#print("Factorial of",num,"is",factorial(num))

#def factorial(n):
    #if n < 0:
     #   return 0
    #elif n == 0 or n == 1:
     #   return 1
    #else:
     #   fact = 1
    #    while(n > 1):
   #         fact *= n
  #          n -= 1
 #       return fact
# Driver Code
#num = 4
#print("Factorial of",num,"is",factorial(num))

#writa a profram using function for addtion  ,sub,mul,division

#print("Enter First Number: ")
#numOne = int(input())
#print("Enter Second Number: ")
#numTwo = int(input())
#res = numOne+numTwo
#print("\nAddition Result = ", res)
#res = numOne-numTwo
#print("Subtraction Result = ", res)
#res = numOne*numTwo
#print("Multiplication Result = ", res)
#res = numOne/numTwo
#print("Division Result = ", res)

 
#pro to enter the name and percentage of marks in a dictionary and display info on the screen 
#n = int(input("Enter number of students: "))
#result = {}
#for i in range(n):
# print("Enter Details of student No.", i+1)
#rno = int(input("Roll No: "))
#name = input("Name: ")
#marks = int(input("Marks: "))
#result[rno] = [name, marks]
#print(result)



def student(x,y,z):
   result = {}
   result[roll_no] = [std_name, marks]
   print(result)
num = int(input("nter No of Students:"))
for i in range(num):
   roll_no = int(input("Roll No: "))
   std_name = input("Student Name: ")
   marks = int(input("Marks: "))
   student(std_name, roll_no, marks)


