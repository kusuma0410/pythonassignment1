#13/02/24 
#set mathamatical operations:

# #union
# # this will return common elements from the two sets

#s1={10,20,30,40,50,60,70,80}
#s2={10,20,40,90,100,110,120,130}
#print(s1.union(s2)) #o/p:{130, 100, 70, 40, 10, 110, 80, 50, 20, 120, 90, 60, 30}
#print(s1|s2)

#s1={"apple","ntr","balaya"}
#s2={"apple","banana","balaya","cherry","ntr"}
#print(s1.union(s2)) #o/p:{'cherry', 'ntr', 'balaya', 'apple', 'banana'}

#s1={1,2,3,4,5,6,7,8,9}
#s2={1,2,4,9,10,11,12,13}
#print(s1.union(s2)) #o/p:{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

# #intersection
#s1={10,20,30,40,50,60,70,80}
#s2={10,20,40,90,100,110,120,130}
#print(s1.intersection(s2))  #o/p:{40, 10, 20}

#s1={"apple","ntr","balaya"}
#s2={"apple","banana","balaya","cherry","ntr"}
#print(s1.intersection(s2)) #o/p:{'balaya', 'ntr', 'apple'}

#s1={1,2,3,4,5,6,7,8,9}
#s2={1,2,4,9,10,11,12,13}
#print(s1.intersection(s2)) #o/p:{1, 2, 4, 9}

# #diffrence
#s1={10,20,30,40,50,60,70,80}
#s2={10,20,40,90,100,110,120,130}
#print(s1.difference(s2)) #o/p:{70, 80, 50, 60, 30}

#s1={"apple","ntr","balaya"}
#s2={"apple","banana","balaya","cherry","ntr"}
#print(s1.difference(s2)) #o/p:set()

#s1={1,2,3,4,5,6,7,8,9}
#s2={1,2,4,9,10,11,12,13}
#print(s1.difference(s2)) #o/p:{3, 5, 6, 7, 8}

# #sysmetric diff

#s1={10,20,30,40,50,60,70,80}
#s2={10,20,40,90,100,110,120,130}
#print(s1.symmetric_difference(s2)) #o/p:{130, 100, 70, 110, 80, 50, 120, 90, 60, 30}

#s1={"apple","ntr","balaya"}
#s2={"apple","banana","balaya","cherry","ntr"}
#print(s1.symmetric_difference(s2)) #o/p:{'cherry', 'banana'}

#s1={1,2,3,4,5,6,7,8,9}
#s2={1,2,4,9,10,11,12,13}
#print(s1.symmetric_difference(s2)) #o/p:{3, 5, 6, 7, 8, 10, 11, 12, 13}

# s={x*x for x in range(12) if x%2==0}
# print(s)

#dict data type 
# d={}
# d=dict()
# d[key]=value
# print(type(d))

# d={}
# name=input
# marks=input
# d[100]=99
# d[200]=88

# print(d)
# print(d[100])

#how to update the dictionaris 

#d={100:"aman",200:"raju",300:"ram"}
#d[800]="laxhman"
#print(d) #o/p:{100: 'aman', 200: 'raju', 300: 'ram', 800: 'laxhman'}

#d={100:"aman",200:"raju",300:"ram"}
#d[100]="laxhman"
#print(d) #o/p:{100: 'laxhman', 200: 'raju', 300: 'ram'}

#delete elements from dict

#d={100:"aman",200:"raju",300:"ram"}
#del d[100]
#print(d) #o/p:{200: 'raju', 300: 'ram'}

#d={100:"aman",200:"raju",300:"ram"}
#del d[200]
#print(d) #o/p:{100: 'aman', 300: 'ram'}

#d={100:"aman",200:"raju",300:"ram"}
#d.clear()
#print(d)

#imp fun /methods of dict

#l=((100,"aman"),(200,"raju"))
#d=dict(l)
#print(d) #o/p:{100: 'aman', 200: 'raju'}

#l=[[100,"aman"],[200,"raju"]]
#d=dict(l)
#print(d)#o/p:{100: 'aman', 200: 'raju'}

#l=([100,"aman"],[200,"raju"])
#d=dict(l)
#print(d) #o/p:{100: 'aman', 200: 'raju'}

#l=({100,"aman"},{200,"raju"})
#d=dict(l)
#print(d) #o/p:{'aman': 100, 200: 'raju'}

#l={{100,"aman"},{200,"raju"}}
#d=dict(l)
#print(d) #o/p:TypeError: unhashable type: 'set'

# d={100:"aman",200:"raju",300:"ram"}
# print(len(d))


#get()
#d={100:"aman",200:"raju",300:"ram"}
#print(d.get(100)) #o/p:aman
#print(d.get(800)) #o/p:None
#print(d[800]) #o/p:KeyError: 800

#pop()
#d={100:"aman",200:"raju",300:"ram"}
#print(d.pop(200)) #o/p:raju
#print(d.pop(400)) #o/p:KeyError: 400

# popitem
#d={100:"aman",200:"raju",300:"ram"}
#print(d.popitem()) #o/p:(300, 'ram')
#print(d.popitem(100)) #o/p:TypeError: dict.popitem() takes no arguments (1 given)

#keys()
#d={100:"aman",200:"raju",300:"ram"}
#print(d.keys()) #o/p:dict_keys([100, 200, 300])

#d={"aman","raju","ram"}
#print(d.keys()) #o/p:AttributeError: 'set' object has no attribute 'keys'

#d={10,30,40}
#print(d.keys()) #o/p:AttributeError: 'set' object has no attribute 'keys'

#d=(10,30,40)
#print(d.keys())#o/p:AttributeError: 'tuple' object has no attribute 'keys'

# #vales
#d={100:"aman",200:"raju",300:"ram"}
#print(d.values()) #o/p:dict_values(['aman', 'raju', 'ram'])

#d={"aman","raju","ram"}
#print(d.values()) #o/p:AttributeError: 'set' object has no attribute 'values'

#d={10,30,40}
#print(d.values()) #o/p:AttributeError: 'set' object has no attribute 'values'

#items() (k,v)
#d={100:"aman",200:"raju",300:"ram"}
 #o/p:dict_items([(100, 'aman'), (200, 'raju'), (300, 'ram')])

#d={"aman","raju","ram"}
#l=d.items()
#print(l) #o/p:AttributeError: 'set' object has no attribute 'items'

# #copy()
# d={100:"aman",200:"raju",300:"ram"}
# d1=d.copy()
# print(d1)

#s1={"apple","banana","balaya","cherry","ntr"}
#s2=s1.copy()
#print(s2) #o/p:{'balaya', 'apple', 'cherry', 'ntr', 'banana'}

#s1={1,2,3,4,5,6,7,8,9}
#s2=s1.copy()
#print(s2) #o/p:{1, 2, 3, 4, 5, 6, 7, 8, 9}

#set defualt

#d={200:"raju",300:"ram"}
#print(d.setdefault(100,"sunny")) #o/p:sunny    {200: 'raju', 300: 'ram', 100: 'sunny'}
#print(d)

#d={100:"raju",300:"ram"}
#print(d.setdefault(100,"sunny"))
#print(d) #o/p:raju   {100: 'raju', 300: 'ram'}

#update()
#d={100:"aman",200:"raju",300:"ram"}
#d1={1:"apple",2:"mangoes"}
#d.update(d1)
#print(d) #o/p:{100: 'aman', 200: 'raju', 300: 'ram', 1: 'apple', 2: 'mangoes'}

#d={100:"chiru",200:"ntr",300:"ram"}
#d1={1:"ramcharan",2:"sita"}
#d.update(d1)
#print(d) #{100: 'chiru', 200: 'ntr', 300: 'ram', 1: 'ramcharan', 2: 'sita'}

d={100:"banana",200:"cherry",300:"rose"}
d1={1:"apple",2:"mangoes"}
d.update(d1)
print(d)
