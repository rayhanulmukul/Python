def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)
def lcm(a, b):
    mul = a * b
    var = gcd(a, b)
    return mul // var

t = int(input())
while t:
    n, m = map(int, input().split())
    print("Gcd = {} lcm = {}".format(gcd(n, m), lcm(n, m)))
    t = t - 1