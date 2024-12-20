f = open('day_19_input.txt','r')
lines = f.readlines()
lines = [x.strip() for x in lines]

patterns = []
input = []
switch = False
for line in lines:
    if line == '':
        switch = True
        continue
    if switch:
        input += [l.strip() for l in line.split(",")]
    else:
        patterns += [l.strip() for l in line.split(",")]
    
#-----------part 1--------------------------------------

def backtracking(rest, path):
    if len(rest) == 0:
        return True
    for pattern in patterns:
        if rest.startswith(pattern):
            path.append(pattern)
            if backtracking(rest[len(pattern):], path):
                return True
            path.pop()
    return False

count = 0
for item in input: 
    if backtracking(item, []):
        count+=1
print(count)
    
#-----------part 2--------------------------------------
#memoization
def backtracking2(rest, memory):
    if rest in memory:
        return memory[rest]
    if len(rest) == 0:
        return 1
    total_combinations = 0
    for pattern in patterns:
        if rest.startswith(pattern):
            total_combinations += backtracking2(rest[len(pattern):], memory)
    memory[rest] = total_combinations
    return total_combinations

count = 0
for item in input:
    memo = {}
    count += backtracking2(item, memo)

print(count)
