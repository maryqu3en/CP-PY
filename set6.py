ùgit ù# Duplicate Encoder -------------------------------------------------------------------
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


# Crack the PIN
from hashlib import md5
def crack(hash):
    PIN = 0
    while True:
        if hash == md5(str(PIN).zfill(5).encode()).hexdigest():
            return str(PIN).zfill(5)
        PIN += 1
        
    
    