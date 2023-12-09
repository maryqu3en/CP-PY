# Basic Encryption --------------------------------------------------------
def encrypt(text, rule):
    return "".join(chr((ord(char) + rule) % 256) for char in text)


# Highest Scoring Word ----------------------------------------------------
def high(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = x.split()
    max_score = 0
    max_word = ""
    for word in x:
        word_score = sum(alphabet.index(char) + 1 for char in word)
        if word_score > max_score:
            max_score = word_score
            max_word = word
    return max_word




# testing ------------------------------------------------

print(chr((ord("a")+1)%256))
print(encrypt("hello world!", 4))

print("hello world ->", high("hello world"))