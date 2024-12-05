f = open('day_5_input.txt','r')
lines = f.readlines()
lines = [line.strip() for line in lines]

divider = lines.index('')

rules = lines[:divider]
updates= lines[divider+1:]

rules = [r.split('|') for r in rules]
updates = [(u).split(',') for u in updates]

#-----------part 1--------------------------------------
middle_page = []
not_valid_updates = []
for up in updates:
    valid = True
    for i in range(len(up)-1):
        current = up[i]
        next_part = up[i+1:]
        for next in next_part:
            if [current, next] not in rules:
                valid = False
                break
    if valid: 
        middle_page.append(up[len(up)//2])
    else:
        not_valid_updates.append(up)
    
print(sum([int(x) for x in middle_page]))
#-----------part 2--------------------------------------

middle_page2 = []

def fix_update(up, rules):
    for i in range(len(up)-1):
        current = up[i]
        next = up[i+1]
        if [current, next] not in rules:
            up[i], up[i + 1] = next, current
            return fix_update(up, rules)
    return up

for up in not_valid_updates:
    fix_update(up, rules)
    middle_page2.append(up[len(up)//2])

print(sum([int(x) for x in middle_page2]))