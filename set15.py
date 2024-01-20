# Roman Numerals Encoder -----------------------------------------------------------------
def solution(n):
    dic = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    roman = ""
    for x in reversed(dic.keys()):
        while n >= x:
            n -= x
            roman += dic[x]
    return roman
#CLASSIC SOLUTION
    while n > 0:
        if n >= 1000:
            roman += "M"
            n -= 1000
        elif n >= 900:
            roman += "CM"
            n -= 900
        elif n >= 500:
            roman += "D"
            n -= 500
        elif n >= 400:
            roman += "CD"
            n -= 400
        elif n >= 100:
            roman += "C"
            n -= 100
        elif n >= 90:
            roman += "XC"
            n -= 90
        elif n >= 50:
            roman += "L"
            n -= 50
        elif n >= 40:
            roman += "XL"
            n -= 40
        elif n >= 10:
            roman += "X"
            n -= 10
        elif n >= 9:
            roman += "IX"
            n -= 9
        elif n >= 5:
            roman += "V"
            n -= 5
        elif n >= 4:
            roman += "IV"
            n -= 4
        elif n >= 1:
            roman += "I"
            n -= 1
    return roman


# Roman Numerals Decoder
def solution(roman: str) -> int:
    dic = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
    num = 0
    i = 0
    while i < len(roman):
        if i < len(roman) - 1 and roman[i:i+2] in dic:
            num += dic[roman[i:i+2]]
            i += 2
        else:
            num += dic[roman[i]]
            i += 1
    return num