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
reverse_string ("hello!")

