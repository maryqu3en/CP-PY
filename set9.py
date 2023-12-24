# Find the missing letter -----------------------------------
def find_missing_letter(array):
    for i in range(len(array) - 1):
        if ord(array[i + 1]) - ord(array[i]) != 1:
            return chr(ord(array[i]) + 1)


# Valid Braces ---------------------------------------------
def valid_braces(string):
    stack = []
    for e in string:
        if e in '{([':
            stack.append(e)
        elif e in '])}':
            if not stack:
                return False
            top = stack.pop()
            if (e == ')' and top != '(') or (e == '}' and top != '{') or (e == ']' and top != '['):
                return False
    return not stack