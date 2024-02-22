#13/02/24 tuesday
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
