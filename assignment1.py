#nested for loop:31/1/24
#for i in range(4):
 #   for j in range(4):
  #   print("i={}and j={}".format(i,j))

#for i in range(4):
    #for j in range(6):
   #  print("i={}and j={}".format(i,j))

#for i in range(2):
 #   for j in range(6):
  #   print("i={}and j={}".format(i,j))
#transfer statement:
    #1.break:eg1
#for i in range(10):
 #   if i==8:
  #      print("hi")
   #     break
    #print(i)

#eg2:
#for i in range(5):
  #  if i==4:
 #       print("hello")
  #      break
   # print(i)

#eg3:
#for i in range(8):
 #   if i==8:
  #      print("hi")
   #     break
    #print(i)

#eg4:
#num = 0
#for i in range(10): 
    #num += 1
    #if num == 8: 
        #break
 #   print("The num has value:", num) 
#print("Out of value")

#continue:eg1
#l=[10,20,30,150,40,60]
#for i in l:
 #   if i >100:
  #      print("sorry limit excessed")
   #     continue
    #print(i,"is processed")   

#eg2:
#for i in range(5):
  #  if i == 3:
 #       continue
#    print(i)
#eg3:
#for i in range(1, 11):
    #if i == 6:
     #   continue
    #else:
     #   print(i, end=" ")




#pass statement:eg1
#for i in range(10):
 #if i%2==0:
 #  print(i)
#else:
      #pass

#eg2:
#n = 10
#if n > 10:
 #   pass
#print('Hello')

#function in methods of string:
#stip():eg1
#txt = input("enter the friute name")
#txt1=("cherry","banana","mango")
#if txt.strip() in txt1:
 #   print("yes it is available")
#else:
 #   print(txt,"not available")

#eg2:
#shop = input("enter the item name")
#s=("rice","banana","shampoo","soap","vegitables")
#if shop.strip() in s:
 #   print("yes it is available")
#else:
  #  print(shop,"not available")

#lstip():it print endspace also(l means leftstring)
#a= "banana    "
#x = a.lstrip()
#print("of all fruits", x, "is my favorite")

#eg2:
#txt = input("enter the friute name")
#txt1=("cherry ","banana ","mango ")
#if txt.lstrip() in txt1:
 #   print("yes it is available")
#else:
 #   print(txt,"not available")

#rstipe():it print starting space also(r means rightstring)
#k= "  banana"
#x = k.rstrip()
#print("of all fruits", x, "is my favorite")

txt = input("enter the friute name")
txt1=("   cherry","  banana","  mango")
if txt.rstrip() in txt1:
    print("yes it is available")
else:
    print(txt,"not available")