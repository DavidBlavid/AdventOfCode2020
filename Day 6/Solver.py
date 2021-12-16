import string
q, nq, sumQ1, sumQ2 = ([], [], 0, 0)
with open('input.txt') as file:
    for line in file:
        if line == '\n':
            sumQ1, sumQ2 = (sumQ1 + len(q), sumQ2 + 26 - len(nq))
            q, nq = ([], [])
        else:
            for char in line[:-1]:
                if char not in q:
                    q.append(char)
            for nc in string.ascii_lowercase:
                if nc not in line[:-1] and nc not in nq:
                    nq.append(nc)
print(sumQ1)
print(sumQ2)
