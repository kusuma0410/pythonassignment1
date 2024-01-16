#byte array:
#it is mutable(we can change it)
#both bytes and bytesarray are same but only
#difference b/w bytes and bytesarray is immutable and mutable
x=[10,20,30,40]
b=bytearray(x)
type(x)#list
type(b)#bytearray
b[0]
b[0]=120
for i in b:
    print(i)
