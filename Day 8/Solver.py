with open('input.txt') as file:
    instr = [elem[:-1] for elem in file.readlines()]

    for change in range(len(instr)):
        print()
        print('Changed', change)
        pos, acc, visited = (0, 0, [])
        while pos not in visited and pos < 629:
            visited.append(pos)
            i = instr[pos]
            
            if i[0:3] == 'acc':
                #print('[acc]', pos, acc, i[4:])
                acc += int (i[4:])
                
            if (i[0:3] == 'jmp' and not pos == change) or (i[0:3] == 'nop' and pos == change):
                #print('[jmp]', pos, acc, i[4:]) 
                pos += int (i[4:])
            else:
                pos += 1
        if pos not in visited:
            print(pos)
            
    print('THE END', acc, pos)
