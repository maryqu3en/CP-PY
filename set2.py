# FizzBuzz ---------------------------------------------------
def fizzbuzz(n):
    return [("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) or i for i in range(1, n + 1)]



# Sorted? yes? no? how? --------------------------------------
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    if arr == sorted(arr)[::-1]:
        return "yes, descending"
    return "no"


# Printer Errors ---------------------------------------------
def printer_error(s):
    return f"{sum([1 for char in s if char in 'nopqrstuvwxyz'])}/{len(s)}"


# Sum of two lowest positive integers ------------------------
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


# Binary Addition ---------------------------------------------
def add_binary(a,b):
    return format(a + b, 'b')


# Is this a triangle? -----------------------------------------
def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


# Regex validate PIN code -------------------------------------
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


# Tribonacci Sequence -----------------------------------------
def tribonacci(signature, n):
    if n == 0:
        return []
    if n <= 3:
        return signature[:n]
    for i in range(n - 3):
        new = sum(signature[-3:])
        signature.append(new)
    return signature


# The Hashtag Generator ---------------------------------------
def generate_hashtag(s):
    if not s:
        return False
    words = [word.capitalize() for word in s.split()]
    hashtag = "#" + ''.join(words)
    return hashtag if len(hashtag) <= 140 else False


# Convert string to camel case --------------------------------
def to_camel_case(text):
    words = text.replace('-', '_').split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])


