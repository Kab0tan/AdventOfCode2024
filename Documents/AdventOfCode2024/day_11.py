from collections import Counter

f = open('day_11_input.txt','r')
lines = f.readlines()
lines = lines[0].split()

#-----------part 1--------------------------------------

def rules(x):
    if len(x)%2 == 0:
        left = str(int(x[:len(x)//2]))
        right = str(int(x[len(x)//2:]))
        return [left, right]
    elif x == '0':
        return ['1']
    else:
        return [str(int(x)*2024)]

def stone_division(iteration):    
    output = Counter(lines)
    for i in range(iteration):
        new_output = Counter()
        for item, count in output.items():
            output = rules(item)
            for new_item in output:
                new_output[new_item] += count
        output = new_output

    total_count = sum(output.values())
    print(total_count)

stone_division(25)

#-----------part 2--------------------------------------
stone_division(75)
