#read from input
inp = open("input.txt", "r")
nums = inp.readlines()
inp.close()

#convert to int
for i in range(len(nums)):
        nums[i] = int(nums[i][:-1])

#solve part 1
def part1(inputNums):

    for n in inputNums:
        
        find = 2020 - n
        
        for j in inputNums:
            if find == j:
                print(n, " ", find)
                print(n * find)
                break

#solve part 2
def part2(inputNums):

    for n in inputNums:
        
        find_1 = 2020 - n
        
        for j in inputNums:

            find_2 = find_1 - j

            for k in inputNums:

                if find_2 == k:
                    print(n, " ", j, " ", k)
                    print(n * j * k)
                    break
#execute
part1(nums)
part2(nums)
