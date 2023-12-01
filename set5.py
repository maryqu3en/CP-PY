# Who likes it? -----------------------------------------------
# CLASSIC METHOD :
# def likes(names):
#     if not names:
#         return "no one likes this"
#     elif len(names) == 1:
#         return f"{names[0]} likes this"
#     elif len(names) == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
#
# METHOD 2 :
def likes(names):
    match names: 
        case []: return "no one likes this"
        case [a]: return f"{a} likes this"
        case [a, b]: return f"{a} and {b} like this"
        case [a, b, c]: return f"{a}, {b} and {c} like this"
        case [a, b, *rest]: return f"{a}, {b} and {len(rest)} others like this"


# uniq (UNIX style) --------------------------------------------
# def uniq(seq): 
#     filseq = []
#     for i, e in enumerate(seq):
#         if i == 0 or e != filseq[-1]:
#             filseq.append(e)
#     return filseq 
#
# OPTIMIZED :
def uniq(seq): 
	return [e for i, e in enumerate(seq) if i == 0 or e != seq[i-1]]


# Your order, please -------------------------------------------
def order(sentence):
    sentence = sentence.split()
    ordered = [""] * len(sentence)
    for word in sentence :
        for c in word :
            if c.isdigit() :
                ordered[int(c) - 1] = word         
    return ' '.join(ordered)


# Playing with digits -------------------------------------------
def dig_pow(n, p):
    digits = [int(digit) for digit in str(n)]
    s = sum(pow(digit, p + i) for i, digit in enumerate(digits))
    return s // n if s % n == 0 else -1


# Equal Sides Of An Array


# testing -----------------------------------------------------

# print(likes(["meriem", "houda", "serine", "malak"]))