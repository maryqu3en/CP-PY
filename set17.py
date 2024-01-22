# Next Round
def next_round(contestant):
    n, k = contestant[0].split()
    k=int(k)
    nxt = 0
    scores = list(map(int, contestant[1].split()))
    for i in range(len(scores)):
        if scores[i] == 0 or scores[i] < scores[k-1]:
            break
        nxt += 1
    return nxt
# x= []
# x.append("8 5")
# x.append("10 9 8 7 7 7 5 5")
# x.append(input())
# x.append(input())
# print(next_round(x))


# Bit++
def bitplusplus(n):
    x = 0
    for _ in range(n):
        x += 1 if "++" in input() else -1
    return x
# print(bitplusplus(int(input())))


# Domino piling
def domino_piling(m, n):
    return (m*n)//2
# m, n = map(int, input().split())
# print(domino_piling(m, n))


# Petya and Strings
def petya_and_strings(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return 1 if s1 > s2 else -1 if s1 < s2 else 0
# print(petya_and_strings(input(), input()))