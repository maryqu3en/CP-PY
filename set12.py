# Cumulative Triangle ------------------------------------------------------
# NOT OPTIMAL !!!!!!! TIMED OUT
# def cumulative_triangle(n):
#     if n == 1:
#         return 1
#     sum = 0
#     elem = 0
#     for i in range(1, n+1):
#         for j in range (1, i+1):
#             elem +=1
#             if i == n:
#                 sum += elem
#     return sum
# OPTIMIZED VER.
def cumulative_triangle(n):
    start = (n*(n-1))//2 + 1
    end = (n*(n+1))//2
    return n * (start + end) // 2


# One down ----------------------------------------------------------------
def one_down(txt):
    if not isinstance(txt, str):
        return "Input is not a string"
    return "".join([chr((ord(c) - ord(c) - 1) % 26 + ord(c)) if c == "A" or c == "a" else chr(ord(c) - 1) if c.isalpha() else c for c in txt])

# NOT MINE BUT LOVED SM
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
correct = 'ZABCDEFGHIJKLMNOPQRSTUVWXYzabcdefghijklmnopqrstuvwxy'
def one_down(txt):
    return "Input is not a string" if type(txt)!=str else txt.translate(str.maketrans(alpha,correct))



# TESTS -------------------------------------------------------------------
c = "a"
print(chr((ord(c) - ord(c) - 1) % 26 + ord(c)))
