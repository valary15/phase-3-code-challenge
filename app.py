def add_numbers(num1, num2):
    result = num1 + num2
    print(result)
    return result
add_numbers(10, 20)

# is even function
def is_even (number):
    if number % 2 == 0:
        print ("number is even")
        return True
    else:
        print ("number is odd") 
        return False
is_even(60)

#reverse string
def reverse_string(text):
    return text[::-1]

result = reverse_string("happy!")
print(result)

# Function: count_vowels
def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
result = count_vowels ("aeiou")
print (result)

# Function: calculate_factorial
def calculate_factorial(number):
    if number < 0:
        return "Please enter a positive number"

    factorial_result=1 
    for i in range(1,number+1): 
        factorial_result *=i

    return factorial_result
print(calculate_factorial(11))

# Function: apply_decorator
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper


def apply_decorator(func):
    return decorator_func(func)

# Sequences: Sort List of Tuples
def sort_by_age(lst):
    return sorted(lst, key=lambda x: x[1])

# Sets and Dictionaries: Merge Dictionaries
def merge_dicts(dict1,dict2):
    total_dict={}
    for key in dict1:
        if key in total_dict:
            total_dict[key] +=dict1[key]
        else:
            total_dict[key]=dict1[key]

    for key in dict2:
        if key in total_dict:
            total_dict[key] +=dict2[key]
        else:
            total_dict[key]=dict2[key]

    return total_dict

# Object-Oriented Programming: Class Creation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
