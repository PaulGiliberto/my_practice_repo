'''# list
cart=["apples", "bananas", "cherries"]
print(cart)

cart.append("donuts")
cart.append("eggs")
cart.append("flour")
print(cart)

cart.remove("cherries")
if "cherry" in cart:
    cart.remove("cherries")
print(cart)

cart.pop(2)
print(cart)
cart.pop()
print(cart)

cart.reverse()
print(cart)
cart.sort()
print(cart)

cart.append("bananas")
cart.append("grapes")
cart.append("oranges")

fruit_basket=cart[3:]
print(fruit_basket)
print(cart)

squares=[]
for i in range(1,11):
    squares.append(i*i)
print(squares)

# comprehension --> could write as [x for x in squares if x ....]

squares=[i*i for i in range(1,11)]
print(squares)

b_items=[item for item in cart if item.startswith("b")]
print(b_items)

lst=['1','10','100']
num_lst=[int(x) for x in lst]
print(num_lst)

inventory=[0]*len(cart)
print(inventory)
inventory[0]=1
print(inventory)

# sets
empty=set()
nums_set={1,1,3,4}
nums_set.add(5)
nums_set.add(10)
print(nums_set)
lst=[1,2,2,3,3,4]
unique=set(lst)
print(unique)
unqiue=list(unique)
print(unique)

st={4,10,3,7,8}
print(st)
sorted(st)
print(st)

# dictionary
fav_snacks={}
fav_snacks={
    "kathleen":"tortilla chips",
    "paul":"ice cream",
    "emily":"buffalo chicken dip",
    "reena":"curry"
}
print(fav_snacks)
fav_snacks["lucas"]="chocolate"
print(fav_snacks)

for key in fav_snacks:
    print(f"{key}'s favorite snack is {fav_snacks[key]}")
    print(key+"'s"+ " favorite snack is "+ fav_snacks[key])

for key,value in fav_snacks.items():
    print(key, value)

if "Bob" in fav_snacks:
    print("Bob's fav snack is "+fav_snacks["Bob"])
else:
    fav_snacks["Bob"]="chips"

keys=fav_snacks.keys()
values=fav_snacks.values()
print(sorted(keys))
print(sorted(values))

fav_snacks["Alice"]=["chips","nuts"]
print(fav_snacks)
'''
