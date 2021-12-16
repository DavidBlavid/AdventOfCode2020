minT = 999999
with open('input.txt') as file:
    lines = file.readlines()
    ts = int(lines[0])
    fbl = [e.strip() for e in lines[1].split(',')]
    bl = [int(e) for e in fbl if e != 'x']

    print(ts)
    print(fbl)
    print(bl)

    m = 1

    for b in bl:
        if b - ts % b < minT:
            minT = b - ts % b
            minB = b
        m *= b

    print(m)

    c = 0
    cSum = 0

    for b in range(len(bl)):
        print('----')
        c = m / bl[b]
        
        while c%b != 1:
            c *= (c%b)
            print(c)

        cSum += c

    print(cSum)
    


print(minT * minB)    
print('gotem')
