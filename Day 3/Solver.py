inp = open("input.txt", "r")
lines = inp.readlines()
inp.close()
treeProduct = 1
for i in [[1, 1],[3, 1],[5,1],[7,1],[1,2]]:
                xPos = yPos = currentTrees = 0
                while yPos < 323:
                        xPos, yPos = (i[0] + xPos, i[1] + yPos)
                        currentTrees += int(yPos < 323 and lines[yPos][xPos%31] == "#")
                treeProduct *= currentTrees

print(treeProduct)
