k = ['a', 'b', 'c']
print(k)#o/p:['a', 'b', 'c']


k= [1,2,3,4,5]
print("List before reverse : ",k)#o/p:List before reverse :  [1, 2, 3, 4, 5]
k.reverse()
print("List after reverse : ",k)#o/p:List after reverse :  [5, 4, 3, 2, 1]


k= ['a','b','c','d']
k.reverse()
print(k)#o/p:['d', 'c', 'b', 'a']

original_list = [1, 2, 3, 4, 5]
print("List before reverse : ",original_list)#o/p:List before reverse :  [1, 2, 3, 4, 5]
reversed_list = []
for value in original_list:
  reversed_list = [value] + reversed_list
print("List after reverse : ", reversed_list)#o/p:List after reverse :  [5, 4, 3, 2, 1]

k= [1, 2, 3, 4, 5]
print("List before reverse : ",k)#o/p:List before reverse :  [1, 2, 3, 4, 5]
reversed_list = []
for value in k:
  reversed_list = [value] + reversed_list
print("List after reverse : ", reversed_list)#o/p:List after reverse :  [5, 4, 3, 2, 1]


k= ['x','y','z']
print("List before reverse : ",k)
reversed_list = []
for value in k:
  reversed_list = [value] + reversed_list
print("List after reverse : ", reversed_list)


#k= [1, 2, 3, 4, 5]
#print("List before reverse : ",k)#o/p:List before reverse :  [1, 2, 3, 4, 5]
#print("List after reverse : ", k[::-1])#o/p:List after reverse :  [5, 4, 3, 2, 1]

#k= ['a','b','c']
#print("List before reverse : ",k)#List before reverse :  ['a', 'b', 'c']
#print("List after reverse : ", k[::-1])#List after reverse :  ['c', 'b', 'a']


#k= [1, 2, 3, 4, 5]
#print("List before reverse : ",k)#o/p:List before reverse :  [1, 2, 3, 4, 5]
#print("List after reverse : ", k[1:3])#o/p:List after reverse :  [2, 3]