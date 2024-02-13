#2/12/24 monday
#t=(10,20,30,40)  #o/p:4
#t=10, #o/p:1
#t=10,"abc" #o/p:2
#t="abc" #o/p:3
#t=("abc") #o/p:3
#t=("apple","banana") #o/p:2
#t="apple","banana"
#print(len(t))

#tuple functions
#len()
#max()
#min()
#sum()
#sorted()
#Python tuples concatenation

#len()
#a=(10,20,55,44,34,9,6) #first tuple
#print(len(a))#display the length of the list

#k=('a','b','c','d','e','f')#o/p:6
#print(len(k))

#s=("apple","banana","abc","xyz",10)
#print(len(s))#o/p:5

#max():
#a=(12,3,4,44,2,34,6) #o/p:44
#print(max(a)) #display max element from the tuple

#k=("apple") 
#print(max(k))#o/p:p

#a=('abcd') 
#print(max(a))#o/p:d   it print last value

#a=("abcde","apple","banana","cherry") 
#print(max(a))#o/p:cherry

#min()
#a=(12,3,4,44,2,34,6) #o/p:2
#print(min(a)) #display min element from the tuple

#k=("apple") 
#print(max(k))#o/p:p

#a=('abcd') 
#print(max(a))#o/p:d   it print last value

#a=("abcde","apple","banana","cherry") 
#print(max(a))#o/p:cherry

#sum()
#a=(12,3,4,44,2,34,6) #o/p:105
#print(sum(a)) #display sum of the elements in the tuple
#a=(10,1,5,4)
#print(sum(a))#o/p:20

#sorted()
#a=(12,3,4,44,2,34,6) #o/p:[2, 3, 4, 6, 12, 34, 44]
#print(sorted(a)) #display sorted tuple

#k=('a','c','d','b','e','g','f')
#print(sorted(k))#o/p:['a', 'b', 'c', 'd', 'e', 'f', 'g']

#k=("a",'p','p','l','e')
#print(sorted(k))#o/p:['a', 'e', 'l', 'p', 'p']

#k=("apple")
#print(sorted(k))#['a', 'e', 'l', 'p', 'p']

#concatenation
#a=(10,20,55,44,34,9,6) #first tuple
#b=(1,2,3) # second tuple
#print(a+b) #python tuples concatenation  o/p:(10, 20, 55, 44, 34, 9, 6, 1, 2, 3)
#print(b*4) #python tuples replication     o/p:(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)

#COPY() #to create a clone objects
# s1={10,20,30,40}
# s2=s1.copy()
# print(s2)

#k1={"apple","banana","abc"}
#k2=k1.copy()
#print(k2) #o/p:{'apple', 'abc', 'banana'}

#pop()
#s={10,20,30,40}
#print(s.pop()) #o/p:40
#k={"apple","balaya","ntr","abc"}
#print(k.pop()) #o/p:balaya

# remove()
#s={10,30,40,50,60,70}
#s.remove(100)
#print(s) #o/p:KeyError: 100

#discard()
#s={10,30,40,50,60,70}
#s.discard(140)
#print(s) #o/p:{50, 70, 40, 10, 60, 30}
#s.discard(30)
#print(s) #o/p:{50, 70, 40, 10, 60}

#clear()
#s={10,30,40,50,60,70}
#s.clear()
#print(s) #o/p:set()

#discard()
#The discard() method removes the specified item from the set. 
#This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

#pop():
#The pop() function removes the last element or the element based on the index given.
#It does not require a parameter; it is optional.
#It returns the value of the deleted element.
#Syntax: list_name.pop()
#Time complexity is O(1) when the last element is to be removed. Otherwise, it is O(n) for extracting an element at the specified index.
#    It gives IndexError if the specified index is not found
#It gives no error if the parameter is not passed.

#remove():
#remove() function removes the first occurrence of the specified element.
#It requires a parameter. The value of the element is passed as the parameter.
#It does not return any value.
#Syntax: list_name.remove(value)
#Time complexity is O(n)
#It gives ValueError if the specified value is not found.
#It throws TypeError if the parameter is not passed.
