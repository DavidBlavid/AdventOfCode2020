with open('input.txt') as file:
    instr = [elem[:-1] for elem in file.readlines()]
    for c in range(len(instr)):
        pos, acc, visited = (0, 0, [])
        while pos not in visited and pos < len(instr):
            visited.append(pos)
            i = instr[pos]
            acc += int(i[4:])*(i[0] == 'a')
            if (i[0] == 'j' and pos != c) or (i[0] == 'n' and pos == c):
                pos += int(i[4:])
            else:
                pos += 1
        if pos in visited:
            print('[' + str(c) + '] looped at', pos, 'acc:', acc)
        else:
            print('[' + str(c) + '] finished at', pos, 'acc:', acc)
