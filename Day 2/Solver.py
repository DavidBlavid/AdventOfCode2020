#read from input
inp = open("input.txt", "r")
lines = inp.readlines()
inp.close()

#counts the number of valid entries
counter = 0

def test1(start, end, c, text):
        found = 0
        for c in text:
                if c == char:
                        found += 1
        return found >= start and found <= end:

def test2(start, end, c, text):
        print(c, text[start-1], text[end-1])
        return ((text[start-1] == c) != (text[end-1] == c))

#for position in range(5):
for position in range(len(lines)):

        #the end of the starting parameter
        startIndex = lines[position].find('-', 0)
        start = int(lines[position][0:startIndex])

        #the end of the ending parameter
        endIndex = lines[position].find(' ', 0)
        end = int(lines[position][startIndex + 1:endIndex])

        #the position of the char parameter
        charIndex = lines[position].find(':', 0) - 1
        char = lines[position][charIndex]

        #the start of the text
        textIndex = lines[position].find(' ', charIndex) + 1
        text = lines[position][textIndex:len(lines[position]) - 1]

        #saves how many chars were found in text
        found = 0

        #choose test1 or test2 here
        if test2(start, end, char, text):
                #increment counter if valid entry found
                counter += 1

print(counter)
