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


# Which are in?

array1 = ["arp", "live", "strong"]

array2 = ["lively", "alive", "harp", "sharp", "armstrong"]
array2 = ' '.join(array2)
print(array2)

print([word for word in array1 if word in array2])
