# The Hashtag Generator --------------------------------------
def generate_hashtag(s):
    if not s:
        return False
    words = [word.capitalize() for word in s.split()]
    hashtag = "#" + ''.join(words)
    return hashtag if len(hashtag) <= 140 else False


# Matrix Transpose -------------------------------------------
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


# Persistent Bugger ------------------------------------------
def persistence(n):
    persistence_count = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        persistence_count += 1
    return persistence_count


# Bit Counting -----------------------------------------------
def count_bits(n):
    return format(n, 'b').count('1')


# Leap Years -------------------------------------------------
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


# Counting Duplicates -----------------------------------------
from collections import Counter
def duplicate_count(s):
    char_count = Counter(char.lower() for char in s if char.isalnum())
    return sum(count > 1 for count in char_count.values())