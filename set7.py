# Unique In Order -------------------------------------------------------------
def unique_in_order(seq):
   	return [e for i, e in enumerate(seq) if i == 0 or e != seq[i-1]]


# Find the unique number ------------------------------------------------------
def find_uniq(arr):
    uni = arr[0]
    if arr.count(uni) == 1:
        return uni
    for e in arr:
        if e != uni:
            return e
        

# Replace With Alphabet Position -----------------------------------------------
def alphabet_position(text):
    alphabit = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    result = ""
    for char in text:
        if char.isalpha():
            result += str(alphabit.index(char) + 1) + ' '
    return result.strip()