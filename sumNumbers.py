def sum1(n):
    return (n) * (n + 1) // 2

def sum2(n):
    sm = 0
    for i in range(1, n + 1):
        sm += i
    return sm

t = int(input())
while t:
    n = int(input())
    print("Sum1 executed output {}".format(sum1(n)))
    print("Sum2 executed output {}".format(sum1(n)))
    t = t - 1