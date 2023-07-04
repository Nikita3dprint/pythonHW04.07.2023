for n in range(1, 200):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + '01'
    else:
        b = b + '10'
    r = int(b, 2)
    if r > 73:
        print(r)
        break
