bags = {}
count = 0

def subSearch1(elem, depth):

    found = False
    
    if bags[elem] != []:
        
        #print(' ' * depth + '∟ ' + bags[elem])
        
        for el in bags[elem]:
            
            if el[2:] == 'shiny gold':
                print(' ' * depth * 2 + '∟ ++++++++++++++')
                found = True
            
            print(' ' * depth * 2 + '∟ ' + el[2:])
            if not found:
                found = subSearch(el[2:], depth + 1)
                
    print(' ' * depth * 2+ '∟ XXX' * (not found) + '∟ ✓✓✓' * found)
    return found        

def subSearch2(elem, depth):
    
    found = 0

    if bags[elem] != []:
        
        for el in bags[elem]:
            print(' ' * depth * 2 + '∟ ' + el)
            found += subSearch2(el[2:], depth + 1) * int(el[0])
            found *= int(el[0])
    else:
        return 0
    print(' ' * depth + '->' + str(found))
    return found 

with open('input.txt') as file:
    for line in file:
        spl = line.split()
        add = []

        for i in range(int((len(spl) - 4) / 4)):
            pos = (i * 4) + 4
            add.append(spl[pos] + '.' + spl[pos + 1] + ' ' + spl[pos + 2])
        bags[spl[0] + ' ' + spl[1]] = add

    #print(bags)

   # for el in bags:
        #print('------')
        #print(el)
        #if subSearch(el, 0):
            #count += 1
        #print(subSearch2(el, 0))

    print(subSearch2('shiny gold', 0))
            
#print(bags)
