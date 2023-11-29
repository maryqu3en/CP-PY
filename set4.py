# Encrypt this! ----------------------------------------------------
def encrypt_this(text):
    text = text.split()
    for i, word in enumerate(text):
        if word:
            if len(word) == 1:
                word = str(ord(word))
            elif len(word) == 2:
                word = str(ord(word[0])) + word[1]
            else:
                word = str(ord(word[0])) + word[-1] + word[2:-1] + word[1]
            text[i] = word
    return ' '.join(text)


# Decipher this! ---------------------------------------------------
def decipher_this(s):
    s = s.split()
    for i, word in enumerate(s):
        ascii=""
        rword=""
        for c in word :
            if c.isdigit() :
                ascii += c
            else :
                rword += c
        ascii = int(ascii)
        if len(word) > 1:
            original = chr(ascii) + rword[-1] + rword[1:-1] + rword[0] if len(rword) > 1 else chr(ascii) + rword
        else:
            original = chr(ascii)
        s[i] = original
    return ' '.join(s)
            

# Find The Parity Outlier -------------------------------------------
def find_outlier(integers):
    even_count = odd_count = last_even = last_odd = 0
    for num in integers:
        if num % 2 == 0:
            even_count += 1
            last_even = num
        else:
            odd_count += 1
            last_odd = num
    return last_even if even_count == 1 else last_odd


# Extract the domain name from a URL ---------------------------------
def domain_name(url):
    return url.split("www.")[1].split(".")[0] if "www" in url else url.split("//")[1].split(".")[0] if "://" in url else url.split(".")[0]



# testing -------------------------------------------------

# message = "Good evening"
# message = encrypt_this(message)
# print("Encripted: ", message)
# print("Decrypted: ", decipher_this(message))

# --------------------------------------------
# url = "https://www.cnet.com"
# url = "http://www.zombie-bites.com"
# url = "http://github.com/carbonfive/raygun"
# print(domain_name(url))
# -------------------------------------------