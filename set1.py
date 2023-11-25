# Dismevowel Trolls ------------------------------------------------------
def disemvowel(string_):
    vowels = "aeouiAEOUI"
    i = 1
    for letter in string_ : 
        if (letter in vowels) : 
            string_ = string_[:i-1] + string_[i:]
        else:
            i += 1
    return string_


# String ends with? ------------------------------------------------------
def solution(text, ending):
    return ending in text[len(text)-len(ending):]


# Square Every Digit -----------------------------------------------------
def square_digits(num):
    if num == 0:
        return 0
    else:
        sqr = 0
        tenp = 1
        while num > 0:
            sqr = sqr + ((num % 10) ** 2) * tenp 
            tenp *= 10 ** (len(str((num % 10) ** 2))) 
            num //= 10
        return sqr


# Get the Middle Character -----------------------------------------------
def get_middle(s):
    if (len(s) % 2) == 0 :
        return s[(len(s) + 1)//2 -1 : (len(s) + 1)//2 +1] 
    return s[len(s)//2]


# Exes and Ohs -----------------------------------------------------------
def xo(s):
    x = "Xx"
    o = "Oo"
    xn = 0
    on = 0
    for char in s :
        if char in x :
            xn +=1
        elif char in o :
            on +=1
    return xn == on


# You're a square! -------------------------------------------------------
def is_square(n):
    if n == 0 :
        return True
    if n < 0 :
        return False
    for i in range(1, int(n ** 0.5) + 1) :
        if (n // i) == i and n % i == 0 :
            return True
    return False 


# List Filtering ---------------------------------------------------------
def filter_list(l):
	newlist = []
	for item in l :
		if isinstance(item, int) :
			newlist.append(item)
	return newlist


# Highest and Lowest -----------------------------------------------------
def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    if not num_list:
        return ""
    return str(max(num_list)) + " " + str(min(num_list))


# Stop gninnipS My sdroW! ------------------------------------------------
def spin_words(sentence):
    words = []
    word = ""
    for char in sentence + " ":
        if char == " ":
            if len(word) >= 5:
                words.append(word[::-1])
            else:
                words.append(word)
            word = ""
        else:
            word += char
    return " ".join(words)


# Jaden casing strings ----------------------------------------------------
def to_jaden_case(string):
    words = []
    word = ""
    for char in string + " ":
        if char == " ":
            word = word.capitalize()
            words.append(word)
            word = ""
        else:
            word += char
    return " ".join(words)

# Complementary DNA ------------------------------------------------------
def DNA_strand(dna):
    complementary_dna = ""
    for char in dna:
        if char == "A":
            complementary_dna += "T"
        elif char == "T":
            complementary_dna += "A"
        elif char == "C":
            complementary_dna += "G"
        elif char == "G":
            complementary_dna += "C"
    return complementary_dna