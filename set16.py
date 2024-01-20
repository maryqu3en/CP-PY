# BOY OR GIRL
def boy_girl(user):
    n = len([c for i, c in enumerate(user) if user[i:].count(c) == 1])
    return "CHAT WITH HER!" if n % 2 == 0 else "IGNORE HIM!"

user = str(input())
print(boy_girl(user))


