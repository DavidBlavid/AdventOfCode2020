with open('input.txt') as file:
    num, fn = ([int(e[:-1]) for e in file.readlines()], 0)
    for i in range(25, len(num)):
        found = False
        for j in num[i-25:i]:
            for k in num[i-25:i]:
                found = found or j + k == num[i] and j != k
        fn = fn if found else num[i]
    print(fn)
    for i in range(0, len(num)):
        s, shift, sMax, sMin = 0, 0, 0, num[i]
        while s < fn:
            s += num[i + shift]
            sMin = min(sMin, num[i + shift])
            sMax = max(sMax, num[i + shift])
            shift += 1
        if s == fn and shift != 1:
            print (sMin + sMax)
