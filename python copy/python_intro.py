print("Hello World!")

# this is single line with a comment

'''
This is a multi line comment
line 2 of comments
'''

#Variables
x=10
x="hello"
x=[1,2,3]
print(x)

x=100
y=10
result=x/y
result=int(result)
print(result)

x=105
result=x//y
print(result)

min_val=min(1,10,50)
print(min_val)
raised=pow(2,3)
print(raised)
raised=2**3
print(raised)

x=-1
y=0
if x<0:
    print("x is negative")
    x=10
elif x>0:
    print("x is positive")
else:
    print("x is 0")

start=10
end=100

if x>=start and x<=end:
    print("x is within range")

if x<start or x>end:
    print("x not within range")

counter=0
while counter<5:
    print(counter)
    counter+=1

for i in range(1,5,2):
    print(i, end=" ")
print()

lst=[2,4,6,8]
for i in range(len(lst)):
    print(i, lst[i], end=" ")
print()

for val in lst:
    print(val)

for index, value in enumerate(lst):
    print(index, value, end=" ")
print()

def hello_world():
    print("Hello World!")
hello_world()

def hello(name):
    print("hello "+name)
    print("Hello",name)
hello("Bob")

def hello2(name="Bob"):
    print("Hello "+name)
hello2()

hello="hello"
for c in hello:
    print(c)

course="Platform Computing"
plat=course[:8]
comp=course[9:]
print(plat)
print(comp)
