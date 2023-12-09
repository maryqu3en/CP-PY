# Simple Encryption #1 - Alternating Split ------------------------------------
def decrypt(s, n):
    if not s or n <= 0:
        return s
    length = len(s)
    mid = length // 2
    for _ in range(n):
        first_half = s[:mid]
        second_half = s[mid:]
        s = ''.join(''.join(x) for x in zip(second_half, first_half + ' '))
    return s.rstrip()


def encrypt(text, n):
    if not text or n == 0:
        return text
    for _ in range(n):
        text = text[1::2] + text[::2]
    return text


# Write Number in Expanded Form
def expanded_form(num):
    expanded = []
    i = 1
    while num != 0:
        if num % pow(10, i) != 0:
            expanded.append(str(num % pow(10, i)))
        num -= num % pow(10, i)
        i += 1
    return ' + '.join(expanded[::-1])