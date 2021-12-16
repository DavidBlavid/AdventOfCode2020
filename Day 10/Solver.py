paths = {}
def testPath(current, nums):
    pathCount = 0
    for i in range(1, 4):
        if (current-i) in paths:
            pathCount += paths[current-i]
        if (current-i) == 0 or (current-i) in nums:
            if current-i == 0:
                pathCount += 1
                return pathCount
            elif (current-i) not in paths:
                pc = testPath(current-i, nums)
                if pc != 0:
                    pathCount += pc
    return pathCount

with open('input.txt') as file:
    nums = [int(e[:-1]) for e in file.readlines()]
    mj = max(nums) + 3
    nums.sort()

    for i in nums:
        pc = testPath(i, nums)
        paths[i] = pc
        print(i, pc)
    #print(ret)
    #print(ret[1]*ret[2])

    j1, j3, l = (0, 0, 0)

##    for i in nums:
##        print('[' + str(i) + ']')
##        if (i - l) == 1:
##            j1 += 1
##            print(j1, j3)
##        if (i - l) == 3:
##            j3 += 1
##            print(j1, j3)
##        l = i
##
##    print(j1, j3, j1*j3)

print('gotem')
