e = n = d = ae = an = 0    
we, wn = 10, 1

for i in open('input.txt').readlines():
    v, c = int(i[1:]), i[0]
    ce = v * (int(c == 'E') - int(c == 'W'))
    cn = v * (int(c == 'N') - int(c == 'S'))
    cd = v / 90 * (int(c == 'R') - int(c == 'L')) % 4
    e += v * (c == 'F') * (int(d == 0.) - int(d == 2.))
    n += v * (c == 'F') * (int(d == 3.) - int(d == 1.))
    d = (cd + d) % 4
    for i in range(int(cd)):
        we, wn = wn, -we
    e, we = e+ce, we+ce
    n, wn = n+cn, wn+cn
    ae += we * v * (c == 'F')
    an += wn * v * (c == 'F')

print(abs(e) + abs(n))
print(abs(ae) + abs(an))
