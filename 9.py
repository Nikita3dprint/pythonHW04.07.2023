for n in range(200, 1, -1):
    b = bin(n)[2:]
    b = b + b[-2]
    b = b + b[1]
    r = int(b, 2)
    if r <= 190:
        print(r)
        break
