#example:print '+' vlue
print([x for x in range(10,0,-1)])#o/p:[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#eg2:
print(*range(10, 0, -1), sep='\n')
#eg3:using forlop 
for i in range(10, 0, -1): 
    print(i)      
#eg3:
for i in range(10): 
   print(10-i) 

#example:print '-' vlue
print([x for x in range(-10,-0,1)])#o/p:[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

#eg2:
print([x for x in range(-20,-10,1)])#o/p:[-20, -19, -18, -17, -16, -15, -14, -13, -12, -11]
#eg3:
print([x for x in range(-40,-20,1)])
#eg4:using forloop
for i in range(-10, -0, 1): 
    print(i)   
#eg5:
for i in range(-20, -10, 1): 
    print(i)    
