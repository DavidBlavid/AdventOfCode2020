import numpy as np
f = np.array(range(0, 1023))
lR, uR, lC, uC, mID = (0, 127, 0, 7, 0)
with open('input.txt') as fl:
    for l in fl:
        for c in l:
            if c == 'F':
                uR -= ((uR - lR) + 1) / 2
            if c == 'B':
                lR += ((uR - lR) + 1) / 2
            if c == 'L':
                uC -= ((uC - lC) + 1) / 2
            if c == 'R':
                lC += ((uC - lC) + 1) / 2         
            if c == '\n':
                f = f[f != int(lR * 8 + lC)]
                mID = max(mID, int(lR * 8 + lC))
                lR, uR, lC, uC = (0, 127, 0, 7)
print(mID)
print(f)
