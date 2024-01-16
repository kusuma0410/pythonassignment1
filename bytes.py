#bytes:
#it is immutable(by mistake we have to try to change it than it will show error)
#it represents "a group of byte numbers"
#it must be in range 0 to 256
x=[10,20,30,40]
b=bytes(x)
type(b)
b[0]
b[0:3]
for x in b:
 print(x)
 #bytes not support item adjestment
 x=[10,20,30,40]
 b=bytes(x)
 b[0]=120