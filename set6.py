# Duplicate Encoder -------------------------------------------------------------------
# def duplicate_encode(word):
#     res = []
#     word = word.lower()
#     for c in word:
#         res.append('(' if word.count(c) == 1 else ')')
#     return ''.join(res)
# OPTIMIZED
def duplicate_encode(word):
    word = word.lower()
    return ''.join(['(' if word.count(c) == 1 else ')' for c in word])


# Take a Ten Minutes Walk ---------------------------------------------------------------





# Detect Pangram ------------------------------------------------------------------------
def is_pangram(s):
    alphabit = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    for c in alphabit:
        if c not in s:
            return False
    return True


# Crack the PIN --------------------------------------------------------------------------
from hashlib import md5
def crack(hash):
    PIN = 0
    while True:
        if hash == md5(str(PIN).zfill(5).encode()).hexdigest():
            return str(PIN).zfill(5)
        PIN += 1
        


# Sort the odd ---------------------------------------------------------------------------
def sort_array(src):
    for i in range(len(src)):
        if src[i] % 2 != 0:
            min = i
            for j in range(i + 1, len(src)):
                if src[j] % 2 != 0 and src[j] < src[min]:
                    min = j
            src[i], src[min] = src[min], src[i]
    return src


    
# Moving Zeros To The End -----------------------------------------------------------------
def move_zeros(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]