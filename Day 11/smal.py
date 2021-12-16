import itertools as it

dirs = [i for i in list(it.product(range(-1,2),range(-1,2))) if i!=(0,0)]

def sim_1(b):
    nb, repeat = b.copy(), True
    while repeat:
        for i in range(len(b)):
            for j in range(len(b[i])):
                c = 0
                for k in dirs:
                    if i+k[0] in range(len(b)) and j+k[1] in range(len(b[i])):
                        c += b[i+k[0]][j+k[1]] == '#'
                if b[i][j] == 'L' and not c:
                    nb[i] = nb[i][:j] + '#' + b[i][j+1:]
                if b[i][j] == '#' and c >= 4:
                    nb[i] = nb[i][:j] + 'L' + b[i][j+1:]
        repeat, b = nb != b, nb.copy()
    return sum([l.count('#') for l in b])

def sim_2(b):
    nb, repeat = b.copy(), True
    while repeat:
        for i in range(len(b)):
            for j in range(len(b[i])):
                c = 0
                for k in dirs:
                    p = i+k[0], j+k[1]
                    while p[0] in range(len(b)) and p[1] in range(len(b[1])):
                        if b[p[0]][p[1]] in ('L','#'):
                            c += b[p[0]][p[1]] == '#'
                            break
                        p = p[0]+k[0], p[1]+k[1]
                if b[i][j] == 'L' and not c:
                    nb[i] = nb[i][:j] + '#' + b[i][j+1:]
                if b[i][j] == '#' and c >= 5:
                    nb[i] = nb[i][:j] + 'L' + b[i][j+1:]
        repeat, b = nb != b, nb.copy()
    return sum([l.count('#') for l in b])
                    

with open('input.txt') as file:
    b = [e[:-1] for e in file.readlines()]

print(sim_1(b))
print(sim_2(b))
