paths = {0:1}

def testPath(n, nums):
    pc = 0
    for i in range(1, 4):
        if (n-i) in paths:
            pc += paths[n-i]
        elif (n-i) in nums:
            pc += testPath(n-i, nums)
    return pc

with open('input.txt') as f:
    nums = [int(e[:-1]) for e in f.readlines()]
    nums.append(max(nums) + 3)
    nums.sort()
    j1 = j3 = l = 0
    for i in nums:
        j1, j3= (j1+(i-l==1), j3+(i-l==3))
        paths[i], l = (testPath(i, nums), i)

print(j1*j3)
print(paths[max(nums)])
