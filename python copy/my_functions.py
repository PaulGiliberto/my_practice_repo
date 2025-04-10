# Paul Giliberto

def num_list(nums):
    '''
    This function takes a list of numbers as the input, then returns the sum of all of them.
    However, the function will ignore negative numbers in the input and only sum up the positive numbers.
    '''
    positive_nums=[num for num in nums if num>=0]
    # This will only add to positive_nums if num>=0
    return sum(positive_nums) if positive_nums else 0

def greeting(name, age):
    '''
    This function will create a greeting for someone when their name and age is the input.
    I found an easy way to do this is to use return f and then put name and age in the {} brackets.
    '''
    return f"Hello {name}! You are {age} years old."


print(num_list([1,2,3,4,5]))
print(num_list([10,-5,23]))
print(num_list([1,-2,3,-4,5,-6,7,-8,9,-10]))

print(greeting("Taylor", 20))
print(greeting("Nick", 76))
print(greeting("David", 33))



