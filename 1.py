for n in range(1, 200):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = b + '1'
    else:
        b = b + '0'
    if b.count('1') % 2 == 0:
        b = b + '1'
    else:
        b = b + '0'
    r = int(b, 2)
    if r > 54:
        print(r)
        break
