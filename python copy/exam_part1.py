# Paul Giliberto

def repeat_start(s):
    """
    Given a string, return a new string where the first two characters 
    are repeated 
    three times. If the string is shorter than two characters, 
    return the string repeated three times.
    repeat_start("hello") returns "hehehe"
    repeat_start("a") returns "aaa"
    """
    if len(s)>=2:
        firstChars=s[:2]
        newString=firstChars*3
        return newString
    else:
        return s*3
    


def shift_left(lst):
    """
    Given a list, rotate its elements to the left by one position. 
    The last element should become the first.
    shift_left([1, 2, 3, 4]) returns [2, 3, 4, 1]
    shift_left([5]) returns [5]
    """
    if len(lst)<=1:
        return lst
    else:
        return lst[1:]+[lst[0]]
    
    

def count_digits(s):
    """
    Use a comprehension to count the number of digits in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_digits("The year is 2025!") returns 4
    The string function isdigit() returns True if the string is a digit.
    Eg. c='1' c.isdigit() returns True
    """
    return sum(1 for c in s if c.isdigit())
    
    

def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    if len(lst)>1:
        min_index=lst.index(min(lst))
        lst[0], lst[min_index]=lst[min_index], lst[0]
        return lst
    else:
        return lst


    

def build_grades_dict():
    '''
    Create a dictionary where the key is a student's name and the value is
    their grade stored as an integer. 
    Read in the file, grades.txt, store the student's first and last name as 
    the key (first and last name should have a space between them) 
    and their grade as the integer value.
    Your output should read:
     {'Alice Brown': 90, 'Bob Smith': 85, 'Charlie Johnson': 78, 
     'Daisy Lee': 92, 'Evelyn Taylor': 88}
    '''
    grades_dict={}
    with open("grades.txt") as file:
        for line in file:
            info=line.strip().split()
            name=f"{info[0]} {info[1]}"
            grades=int(info[2])
            grades_dict[name]=grades
    return grades_dict
    

# Test Cases
print('repeat_start("hello") expected: hehehe')
print('repeat_start("hello") actual:', repeat_start("hello"))

print('shift_left([1, 2, 3, 4]) expected: [2, 3, 4, 1]')
print('shift_left([1, 2, 3, 4]) actual:', shift_left([1, 2, 3, 4]))

print('count_digits("The year is 2025!") expected: 4')
print('count_digits("The year is 2025!") actual:', count_digits("The year is 2025!"))

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))

print(build_grades_dict())
