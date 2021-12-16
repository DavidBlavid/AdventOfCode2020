import re
fields = correct = 0
with open('input.txt') as file:
    for line in file:
        if(line == '\n'):
            correct, fields = (correct + (fields == 7), 0)
        else:
            for f in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
                if f in line:
                    val = line[line.find(f) + len(f) + 1:line.find(' ', line.find(f))]
                    if f == 'byr':
                        fields += (int(val) > 1919 and int(val) < 2003)
                    elif f == 'iyr':
                        fields += (int(val) > 2009 and int(val) < 2021)
                    elif f == 'eyr':
                        fields += (int(val) > 2019 and int(val) < 2031)
                    elif f == 'hgt':
                        if 'cm' in val:
                            fields += (int(val[:-2]) > 149 and int(val[:-2]) < 194)
                        elif 'in' in val:
                            fields += (int(val[:-2]) > 58 and int(val[:-2]) < 77)
                    elif f == 'hcl':
                        fields += (None != re.match('#([a-f]|[0-9]){6}', val))
                    elif f == 'ecl':
                        fields += (val in ['amb','blu','brn','gry','grn','hzl','oth'])
                    elif f == 'pid':
                        fields += (len(val) == 9)
print(correct)
