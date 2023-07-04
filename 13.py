def sum_num(a):
    a1 = int(a)
    s = 0
    while a1 > 0:
        s = s + a1 % 2
        a1 = a1 // 2
    return bin(s)[2:]


k = 0
for n in range(1, 2000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b1 = sum_num(b)
        b = b + b1
    else:
        b = '1' + b + '00'
    r = int(b, 2)
    if (r >= 500) and (r <= 700):
        k = k + 1
print(k)
