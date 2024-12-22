import numpy as np

f = open('day_22_input.txt','r')
lines = f.readlines()
secrets = [int(line.strip()) for line in lines]
def transform(x):
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x

S = []
for secret in secrets:
    for i in range(2000):
        secret = transform(secret)
    S.append(secret)
print("before np.array",sum(S))
print("after np.array",sum(np.array(S)))




data = np.genfromtxt("day_22_input.txt", dtype=int)
rounds = 2000
res = np.zeros((rounds, len(data)), dtype=int)
for i in range(2000):
    res[i] = data % 10
    data = ((data * 64) ^ data) % 16777216
    data = ((data // 32) ^ data) % 16777216
    data = ((data * 2048) ^ data) % 16777216
print(sum(data))
