for n in range(1, 200):
    b = bin(n)[2:]
    c = b
    if c.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    if c.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    r = int(b, 2)
    if r > 180:
        print(r)
        break

