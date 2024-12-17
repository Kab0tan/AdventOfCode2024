f = open('day_17_input.txt','r')
lines = f.readlines()
lines = [ x.strip() for x in lines]

A,B,C = 0,0,0
program = ''
for line in lines : 
    if 'A' in line:
        A = int(line.split(':')[1])
    if 'B' in line:
        B = int(line.split(':')[1])
    if 'C' in line:
        C = int(line.split(':')[1])
    if 'Program' in line:
        program = line.split(':')[1].strip().split(',')

print(A,B,C,program)
#-----------part 1--------------------------------------
def compute(A,B,C,program):
    i = 0
    output = []
    while i < len(program):
        instruction, literal_operand = program[i], int(program[i+1])
        combo_operand = literal_operand
        if combo_operand == 4:
            combo_operand = A
        elif combo_operand == 5:
            combo_operand = B
        elif combo_operand == 6:
            combo_operand = C
        if instruction == '0':
            A = int(A/2**combo_operand)
            i += 2
        elif instruction == '1':
            B = B ^ literal_operand
            i += 2
        elif instruction == '2':
            B = combo_operand%8
            i += 2
        elif instruction == '3':
            if A == 0:
                i+=2
            else:
                i = literal_operand
        elif instruction == '4':
            B = B ^ C
            i += 2
        elif instruction == '5':
            output.append(str(combo_operand%8))
            i += 2
        elif instruction == '6':
            B = int(A/2**combo_operand)
            i += 2
        elif instruction == '7':
            C = int(A/2**combo_operand)
            i += 2
    return ','.join(output)

# out = compute(A,B,C,program)
# print(out)

#-----------part 2--------------------------------------


# 1 000 000 000 is too low
for A in range(300000000, 1000000000):
    i = 0
    output = []
    found = False
    while i < len(program):
        instruction, literal_operand = program[i], int(program[i+1])
        combo_operand = literal_operand
        if combo_operand == 4:
            combo_operand = A
        elif combo_operand == 5:
            combo_operand = B
        elif combo_operand == 6:
            combo_operand = C
        if instruction == '0':
            A = int(A/2**combo_operand)
            i += 2
        elif instruction == '1':
            B = B ^ literal_operand
            i += 2
        elif instruction == '2':
            B = combo_operand%8
            i += 2
        elif instruction == '3':
            if A == 0:
                i+=2
            else:
                i = literal_operand
        elif instruction == '4':
            B = B ^ C
            i += 2
        elif instruction == '5':
            output.append(str(combo_operand%8))
            if program[:len(output)] != output:
                break
            elif program == output:
                found = True
                break
        elif instruction == '6':
            B = int(A/2**combo_operand)
            i += 2
        elif instruction == '7':
            C = int(A/2**combo_operand)
            i += 2
    if found:
        print('trouvé', A)
        break
