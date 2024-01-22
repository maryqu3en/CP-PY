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