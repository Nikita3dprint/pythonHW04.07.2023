def klv_zero(a):
    a1 = int(a)
    k = 0
    while a1 > 0:
        if a1 % 2 == 0:
            k = k + 1
        a1 = a1 // 2
    return k


def klv_one(c):
    c1 = int(c)
    k = 0
    while c1 > 0:
        if c1 % 2 == 1:
            k = k + 1
        c1 = c1 // 2
    return k


for n in range(200, 1, -1):
    b = bin(n)[2:]
    if klv_zero(b) == klv_one(b):
        b = b + b[-1]
    elif klv_zero(b) > klv_one(b):
        b = b + '1'
    else:
        b = b + '0'
    if klv_zero(b) == klv_one(b):
        b = b + b[-1]
    elif klv_zero(b) > klv_one(b):
        b = b + '1'
    else:
        b = b + '0'
    if klv_zero(b) == klv_one(b):
        b = b + b[-1]
    elif klv_zero(b) > klv_one(b):
        b = b + '1'
    else:
        b = b + '0'
    r = int(b, 2)
    if (r % 4 == 0) and (n < 70):
        print(n)
        break
