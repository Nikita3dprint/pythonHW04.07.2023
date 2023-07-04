def sumnum(a):
    s = 0
    a1 = int(a)
    while a1 > 0:
        s = s + a1 % 2
        a1 = a1 // 2
    c = s % 2
    return bin(c)[2:]


k = 0
for n in range(1, 200):
    b = bin(n)[2:]
    b1 = sumnum(b)
    b = b + b1
    b1 = sumnum(b)
    b = b + b1
    r = int(b, 2)
    if (r >= 20) and (r <= 50):
        k = k + 1
print(k)

