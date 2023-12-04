# What century is it? ---------------------------------------------------------------
def what_century(year):
    year = (int(year) - 1) // 100 + 1
    if year < 20:
        return f"{year}th"
    match year % 10:
        case 1: return f"{year}st"
        case 2: return f"{year}nd"
        case 3: return f"{year}rd"
        case _ : return f"{year}th"


# Which are in? ----------------------------------------------------------------------
def in_array(array1, array2):
    array1 = [e for i, e in enumerate(sorted(array1)) if i == 0 or e != sorted(array1)[i-1]]
    array2 = ' '.join(array2)
    return [word for word in array1 if word in array2]


# 



#testing ------------------------------------------------------------------------------
array1 = ['by', 'or', 've', 'wh', 'wh']
array2 = ['why', 'where', 'whatever', 'orbit', 'ever', 'big', 'by', 'or']
print(in_array(array1, array2))