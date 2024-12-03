import re 

f = open('day_3_input.txt','r')
lines = f.readlines()


#-----------part 1--------------------------------------

pattern = r"mul\(([A-Za-z0-9_]+),([A-Za-z0-9_]+)\)"
s = 0
for line in lines:
    results = re.findall(pattern, line)
    s += sum([ int(x)*int(y) for x,y in results])

print(s)
#-----------part 2--------------------------------------


pattern2 = r"mul\(([A-Za-z0-9_]+),([A-Za-z0-9_]+)\)|don't\(\)|do\(\)"
s2 = 0
curr = 0
for line in lines:
    matches = re.finditer(pattern2, line)
    for match in matches:
        if match.group() == "don't()":
            curr = 1
        elif match.group() == "do()":
            curr = 2
        if (curr == 0 or curr == 2) and match.group() != "do()":
            x, y = re.findall(pattern, match.group())[0]
            s2 += int(x)*int(y)
print(s2)
        
