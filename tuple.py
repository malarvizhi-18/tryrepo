#Tuple => Immutable(values not changable),Surrounded by ()

'''a=(21,6,2.3,True,'Ram')
print(a)
print(type(a))
print(a[0])
print(a[-1])
print(a[0:2])
b=list(a)
print(b)
b.append("Raja")
print(b)
print(type(b))
a=tuple(b)
print(a)
print(type(a))

a=(21,6,2.3,True,'Ram')
for i in a:
    print(i)
if "Raja" in a:
    print("Raja is found")
else:
    print("Not found")
print(len(a))

tup1=('rani')
print(type(tup1))
tup2=('rani',)
print(type(tup2))
#del tup2 #deleting a tuple showa exception
#print(tup2)'''

#Concatenate
p=(1,2,3,4,5)
r=(5,6,7,8,9)
s=p+r
print(s)
print(s.count(5))

m=(21,22,23,24,25)
n=(25,26,27,28,29)
o=m,n
print(o)
print(o[0])    #prints 0th array of tuple (o)
print(o[1])    #prints 1st array of tuple (o)
print(o[0][1]) #prints 0th array 1st index of tuple (o)

x=('Sweety',)*10
print(x)

t=(1,14,59,74)
print(t)
print(max(t))
print(min(t))