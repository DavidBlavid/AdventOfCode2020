import re
f=c= 0
with open('input.txt') as fl:
    for l in fl:
        if(l=='\n'):
            c,f=(c+(f==7),0)
        else:
            for i in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
                if i in l:
                    v = l[l.find(i)+4:l.find(' ', l.find(i))]
                    if i=='byr':
                        f+=(int(v)>1919 and int(v)<2003)
                    elif i=='iyr':
                        f+=(int(v)>2009 and int(v)<2021)
                    elif i=='eyr':
                        f+=(int(v)>2019 and int(v)<2031)
                    elif i=='hgt':
                        if 'cm' in v:
                            f+=(int(v[:-2])>149 and int(v[:-2])<194)
                        elif 'in' in v:
                            f+=(int(v[:-2])>58 and int(v[:-2])<77)
                    elif i=='hcl':
                        f+=(None!=re.match('#([a-f]|[0-9]){6}',v))
                    elif i=='ecl':
                        f+=(v in ['amb','blu','brn','gry','grn','hzl','oth'])
                    elif i=='pid':
                        f+=(len(v)==9)
print(c)
