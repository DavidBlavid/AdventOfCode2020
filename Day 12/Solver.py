e = n = d = ae = an = 0    
we, wn = 10, 1
with open('input.txt') as file:
    inst = [e[:-1] for e in file.readlines()]

for i in inst:
    print('----')
    print(i)
    v, c = int(i[1:]), i[0]
    ce = v * (int(c == 'E') - int(c == 'W'))
    cn = v * (int(c == 'N') - int(c == 'S'))
    e += v * (c == 'F') * (int(d == 0.) - int(d == 2.))
    n += v * (c == 'F') * (int(d == 3.) - int(d == 1.))
    d = (d + v / 90) * (int(c == 'R') - int(c == 'L')) % 4
    
    for i in range(int(v / 90) * (int(c == 'R') - int(c == 'L'))%4):
        we, wn = wn, -we
        print('SWAP', we, wn)

    e, we = e+ce, we+ce
    n, wn = n+cn, wn+cn
    
    ae += we * v * (c == 'F')
    an += wn * v * (c == 'F')

    print(we, wn)
    print(ae, an)

print(abs(e) + abs(n))
print(abs(ae) + abs(an))

print('gotem')
