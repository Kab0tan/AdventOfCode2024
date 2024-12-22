from collections import deque, defaultdict

f = open('day_22_input.txt','r')

lines = f.readlines()
secrets = [int(line.strip()) for line in lines]
#-----------part 1--------------------------------------

def transform(x):
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x

S = 0
for secret in secrets:
    for i in range(2000):
        secret = transform(secret)
    S += secret
print(S)    
#-----------part 2--------------------------------------

dict = defaultdict(int)
for secret in secrets:
    previous = secret % 10
    changes = deque(maxlen=4)
    seen = set()
    for _ in range(2000):
        secret = transform(secret)
        last_digit = secret % 10
        changes.append(last_digit - previous)
        previous = last_digit
        if len(changes) == 4 and tuple(changes) not in seen:
            seen.add(tuple(changes))
            dict[tuple(changes)] += last_digit

print(max(dict.values()))