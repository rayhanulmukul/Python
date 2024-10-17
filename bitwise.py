def mulpow(x, y):
    return x << y
def divpow(x, y):
    return x >> y
t = int(input())
while t:
    x, y = map(int, input().split())
    print(mulpow(x, y))
    print(divpow(x, y))
    t -= 1