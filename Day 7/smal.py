bags, count = ({}, 0)

def subSearch1(elem):
    found = False
    if bags[elem] != []:
        for el in bags[elem]:
            found = (found or el[2:] == 'shiny gold')
            if not found:
                found = subSearch1(el[2:])
    return found        

def subSearch2(elem):
    found = 0
    if bags[elem] != []:
        for el in bags[elem]:
            found += (1 + subSearch2(el[2:])) * int(el[0])
    else:
        return 0
    return found 

with open('input.txt') as file:
    for line in file:
        spl, add = (line.split(), [])
        for i in range(int((len(spl) - 4) / 4)):
            pos = (i * 4) + 4
            add.append(spl[pos] + '.' + spl[pos + 1] + ' ' + spl[pos + 2])
        bags[spl[0] + ' ' + spl[1]] = add
    for el in bags:
        count += subSearch1(el)
        
print(count)
print(subSearch2('shiny gold'))
