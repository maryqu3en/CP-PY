# BOY OR GIRL
def boy_girl(user):
    n = len([c for i, c in enumerate(user) if user[i:].count(c) == 1])
    return "CHAT WITH HER!" if n % 2 == 0 else "IGNORE HIM!"

user = str(input())
print(boy_girl(user))


# Way Too Long Words
def long_words(words):
    for word in words[1:]:
        if len(word) > 10:
            print(word[0] + str(len(word) - 2) + word[-1])
        else:
            return print(word)