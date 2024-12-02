f = open('day_2_input.txt','r')
lines = f.readlines()
lines = [ list(int(y) for y in x.split()) for x in lines]

#-----------part 1--------------------------------------

nb_safe = 0
for line in lines: 
    diff = [ (x - y) for x,y in zip(line[1:], line[:-1]) ]
    incr = all(3>=e>0 for e in diff)
    decr = all(-3<=e<0 for e in diff)
    if incr or decr:
        nb_safe += 1
print(nb_safe)

#-----------part 2--------------------------------------

nb_safe2 = 0
for line in lines:
    diff = [ (x - y) for x,y in zip(line[1:], line[:-1]) ]
    incr = all(3>=e>0 for e in diff)
    decr = all(-3<=e<0 for e in diff)
    if not (incr or decr):
        for i in range(len(line)):
            line_to_process = line.copy()
            del line_to_process[i]
            diffb = [ (x - y) for x,y in zip(line_to_process[1:], line_to_process[:-1]) ]
            incrb = all(3>=e>0 for e in diffb)
            decrb = all(-3<=e<0 for e in diffb)
            if incrb or decrb:
                nb_safe2 += 1
                break
    else:
        nb_safe2 += 1

print(nb_safe2)