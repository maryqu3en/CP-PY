# FizzBuzz
def fizzbuzz(n):
    list=[]
    for i in range(1, n+1) :
        result = ""
        if (i % 3 == 0) :
            result = result + "Fizz"
        if (i % 5 == 0) :
            result = result + "Buzz"
        if (result == "") :
            result = i
        list.append(result)
    return list


# 