# Exercise 1
for i in range(1,21):
    if i%3==0:
        print(i)

# Exercise 2
count=1
sum_even=0
while count<=50:
    if count%2==0:
        sum_even+=count
    count+=1
print(sum_even)

# Exercise 3
numbers=[5,8,2,15,10,3,7]
for num in numbers:
    if num>5:
        print(num,end=" ")
print()

# Exercise 4
def swap(lst):
    tmp=lst[0]
    lst[0]=lst[len(lst)-1]
    lst[len(lst)-1]=tmp

lst=[0,3,8,4,5]
swap(lst)
print(lst)



