from collections import defaultdict

f = open('day_24_input.txt','r')
lines = f.readlines()
lines = [x.strip() for x in lines]
index = lines.index('')

connections = lines[index+1:]


#-----------part 1--------------------------------------

wires = defaultdict(int)
for i in range(index):
    wire = lines[i].split(': ')
    wires[wire[0]] = int(wire[1])
    
resolved = set()
while len(resolved) != len(connections):
    for conn in connections:
        tmp = conn.split(' -> ')
        w1,op, w2 = tmp[0].split(' ')
        new_wire = tmp[1]
        if w1 not in wires or w2 not in wires:
            continue
        if op == 'AND':
            wires[new_wire] = wires[w1] & wires[w2]
        elif op == 'OR':
            wires[new_wire] = wires[w1] | wires[w2]
        elif op == 'XOR':
            wires[new_wire] = wires[w1] ^ wires[w2]
        resolved.add(new_wire)
    

wires = dict(sorted(wires.items()))

output= ''
for key, value in wires.items():
    if key.startswith('z'):
        output += str(value)
print(int(output[::-1], 2))
#-----------part 2--------------------------------------