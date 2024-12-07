import itertools

f = open('day_7_input.txt','r')
lines = f.readlines()
lines = [x.strip().split(':') for x in lines]
lines = [[x[0],x[1].split()] for x in lines]
#-----------part 1--------------------------------------
def which_is_valid(input, operators):
    s = 0
    for line in input:
        result = line[0]
        equation = line[1]
        all_op_combination =list(itertools.product(operators, repeat=len(equation)-1))
        is_valid = False
        for op in all_op_combination:
            comb = [equation[0]]+[op+e for e,op in zip(equation[1:], op)]
            tmp = comb[0]
            for c in comb[1:]:
                tmp = str(eval(tmp+c))
            if tmp == result:
                is_valid = True
        if is_valid:
            s+=int(result)
    return s


print(which_is_valid(lines, ['+', '*']))
#-----------part 2--------------------------------------


def which_is_valid2(input, operators):
    s = 0
    for line in input:
        print(line)
        result = line[0]
        equation = line[1]
        all_op_combination =list(itertools.product(operators, repeat=len(equation)-1))
        is_valid = False
        for op in all_op_combination:
            comb = [equation[0]]+[op+e for e,op in zip(equation[1:], op)]
            tmp = comb[0]
            for c in comb[1:]:
                if '||' in c:
                    tmp += c[2:]
                else:
                    tmp = str(eval(tmp+c))
            if tmp == result:
                is_valid = True
        if is_valid:
            s+=int(result)
    return s

print(which_is_valid2(lines, ['+', '*','||']))
