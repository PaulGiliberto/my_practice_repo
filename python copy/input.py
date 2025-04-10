'''name=input("Enter your name ")
print("Hello,",name)

try:
    num=int(input("Enter a number "))
    print("you entered,",num)
    double=num*2
    print("doubled",double)
except:
    print("number was not entered")
'''

with open("movies.txt") as file:
    for line in file:
        print(line.strip())

with open("heights.txt") as file:
    for line in file:
        info=line.strip().split()
        info[2]=int(info[2])
        print(info)

file_name=input("Enter the name of your file")
print("Your file is",file_name)
with open(file_name) as file:
    count=1
    for line in file:
        print(str(count)+". "+line.strip())
        count+=1
        