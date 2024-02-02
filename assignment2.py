#changing case of a sting(1-02-24)
#write a prgram to find the substring which is present in the main string #by user input
#string=input("Enter string:")
#substr=input("Enter word:")
#if(string.find(substr)==-1):
 #     print("Substring not found in string!")
#else:
 #     print("Substring in string!")

#find():
#k = "Hello, welcome to my world."
#x = k.find("welcome")
#print(x)#o/p:7
#eg2:
#k = "Hello, welcome to my world."
#x = k.find("my")
#print(x)#o/p:18

#index():eg1:
#k1= [4, 55, 64, 32, 16, 32]
#x = k1.index(32)
#print(x)#o/p:3
#eg2:
#k2= ['apple', 'banana', 'cherry']
#x=k2.index("cherry")
#print(x)#o/p:2
#eg3:
#k = "Hello, welcome to my world."
#x = k.index("my")
#print(x)#o/p:18

#rindex()
#txt = "Hello, welcome to my world."
#x = txt.rindex("e")
#print(x)
#eg2:
#txt = "Hello, welcome to my world."
#x = txt.rindex("e", 5, 10)
#print(x)#o/p:8
#eg3:
#txt = "Hello, welcome to my world."
#print(txt.rfind("to"))
#print(txt.rindex("t"))

#isalnum():it is only single word are consider(true)than it will show (false)
#txt = "Company12"
#x = txt.isalnum()
#print(x)#o/p:(true)
#eg:2
#txt = "hello,world"
#x = txt.isalnum()
#print(x)#o/p:false

#isalpha():
#txt = "Company12"
#x = txt.isalnum()
#print(x)#o/p:(true)
#eg:2
#txt = "hello ,world"
#x = txt.isalpha()
#print(x)#o/p:false 
#txt = "12"
#x = txt.isalnum()
#print(x)#o/p:true

#isdigit():it is consider only digits like 123....(not float or string)
#k = "50800"
#x = k.isdigit()
#print(x)#o/p:true
#eg2:
#k = "508.00"
#x = k.isdigit()
#print(x)#o/p:false
#eg3:
#k = "hi"
#x = k.isdigit()
#print(x)#o/p:false

#islower():
#k = "hello world!"
#x = k.islower()
#print(x)#o/p:true

#a = "Hello world!"#o/p:false
#b = "hello 123"#o/p:true
#c = "mynameisabc"#o/p:true
#d  = "my name is Abc"#o/p:false
#e  = "123"#o/p:false
#print(a.islower())
#print(b.islower())
#print(c.islower())
#print(d.islower())
#print(e.islower())

#isupper():
#a = "HELLO WORLD!"#o/p:TRUE
#b = "HELLO 123"#o/p:true
#c = "mynameisabc"#o/p:false
#d  = "MY NAME IS ABC"#o/p:true
#e  = "123"#o/p:false
#print(a.isupper())
#print(b.isupper())
#print(c.isupper())
#print(d.isupper())
#print(e.isupper())

#istitlecase():in this first letter mus be capital
#name = 'Jane Doe'
#k= name.istitle()
#print(k)#o/p:true

#name = 'Abc 123 Xyz'
#k= name.istitle()
#print(k)#o/p:true

#name = 'Abc Xyz'
#k= name.istitle()
#print(k)#o/p:true

#name = 'abc  xyz '
#k= name.istitle()
#print(k)#o/p:false

#string = "Test Test";
#print(string, " title cased -- ", string.istitle())  #True

#string = "Test test"
#print(string, " title cased -- ", string.istitle())  #False

#string = "T"
#print(string, " title cased -- ", string.istitle())  #True

#string = "1T"
#print(string, " title cased -- ", string.istitle())  #True

#string = "1T2t"
#print(string, " title cased -- ", string.istitle())  #False

#isspace:
#a = "   "
#x = a.isspace()
#print(x)#o/p:true

#t = "   s   "
#x = t.isspace()
#print(x)#o/p:false

#upper():
#k="hi,hello"
#s=k.upper()
#print(s)

#lower():
#k="HI,HELLO"
#s=k.lower()
#print(s)

#swapcase(): hEllo in this we given 'h' after capital letter than it print 'e' after capital letter(heLLO)
#k = "Hello My Name Is tiger"
#x = k.swapcase()
#print(x)

#title()
#txt = "Welcome to my world"
#x = txt.title()
#print(x)
 
#txt = "hello b2b2b2 and 3g3g3g"
#x = txt.title()
#print(x)

#capitalise():it is turned into first letter to be cappital
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "3 is my dog age."
x = txt.capitalize()
print (x)

txt = "it is cat.it is dog"
x = txt.capitalize()
print (x)#o/p:It is cat.it is dog
