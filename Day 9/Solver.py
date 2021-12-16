with open('input.txt') as file:
    num = [int(e[:-1]) for e in file.readlines()]
    for i in range(25, len(num)):
        found = False
        for j in num[i-25:i]:
            for k in num[i-25:i]:
                found = found or j + k == num[i] and j != k
        if not found:
            fn = num[i]

    for i in range(0, len(num)):
        s, shift, sMin, sMax = 0, 0, num[i], 0
        while s < fn:
            s += num[i + shift]
            sMin = min(sMin, num[i + shift])
            sMax = max(sMax, num[i + shift])
            shift += 1
        if s == fn and shift != 1:
            for j in range(i, i + shift):
                print('[' + str(j) + ']', num[j])
            print (sMin, '+', sMax, '=', sMin + sMax)

print('gotem')
