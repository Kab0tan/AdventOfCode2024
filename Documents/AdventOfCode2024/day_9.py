f = open('day_9_input.txt','r')
lines = f.readlines()


#-----------part 1--------------------------------------

def convert_to_blocks(line):
    blocks = []
    is_file = True
    id = 0
    for char in line:
        if is_file:
            blocks += [id] * int(char)
            is_file = False
            id += 1
        else:
            blocks += ['.'] * int(char)
            is_file = True
    return blocks

res = convert_to_blocks(lines[0])
print("Before compacting: ",''.join([str(x) for x in res]))
s = 0
reverse_index = len(res)-1
for i, item in enumerate(res):
    # print(i, reverse_index)
    if i == reverse_index:
        s+= i*item
        break
    if item == '.':
        while res[reverse_index] == '.':
            reverse_index -= 1
        res[i] = res[reverse_index]
        s+= i*res[i]
        res[reverse_index] = '.'
        print("Current res: ",''.join([str(x) for x in res]))
        reverse_index -= 1
    else:
        s+= i*item
print("Current res: ",''.join([str(x) for x in res]))
print(s)

s2= 0
for j, item in enumerate(res):
    if item != '.':
        s2+= j*item
print(s2)       



#-----------part 2--------------------------------------