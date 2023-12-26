# Multiples of 3 or 5 ---------------------------------------------------------
def solution(number):
    return sum([i for i in range(1, number) if i % 3 == 0 or i % 5 == 0]) if number > 0 else 0


