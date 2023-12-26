# Cumulative Triangle ------------------------------------------------------
# NOT OPTIMAL !!!!!!! TIMED OUT
# def cumulative_triangle(n):
#     if n == 1:
#         return 1
#     sum = 0
#     elem = 0
#     for i in range(1, n+1):
#         for j in range (1, i+1):
#             elem +=1
#             if i == n:
#                 sum += elem
#     return sum
# OPTIMIZED VER.
def cumulative_triangle(n):
    start = (n*(n-1))//2 + 1
    end = (n*(n+1))//2
    return n * (start + end) // 2


