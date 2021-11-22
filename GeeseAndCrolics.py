n = 64
k = 4
g = 2
f = n // k - 1
for i in range(f):
    a = i
    b = (n - k * a) // g
    print(a, " Кролик(ов) ", b, " Гусь(ей)")