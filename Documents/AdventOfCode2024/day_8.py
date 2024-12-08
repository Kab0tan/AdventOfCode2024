import numpy as np
import itertools

f = open('day_8_input.txt','r')
lines = f.readlines()

lines = np.array([list(x.strip()) for x in lines])

unique_symbol = set()

for line in lines:
    for symbol in line:
        if symbol != '.':
            unique_symbol.add(symbol)

antennas_positions = {}

for symbol in unique_symbol:
    pos = np.where(lines == symbol)
    antennas_positions[symbol] = [(x,y) for x,y in zip(pos[0], pos[1])]

def is_valid(x, y, a, b):
    return 0 <= x < a and 0 <= y < b

#-----------part 1--------------------------------------
def distance(pair, matrix):
    p1,p2 = pair
    an1 = (2*p1[0]-p2[0], 2*p1[1]-p2[1])
    an2 = (2*p2[0]-p1[0], 2*p2[1]-p1[1])
    a,b = matrix.shape
    valid = set()
    if is_valid(an1[0], an1[1], a, b):
        valid.add(an1)
    if is_valid(an2[0], an2[1], a, b):
        valid.add(an2)
    return valid

count = set()
for symbol, positions in antennas_positions.items():
    comb = list(itertools.combinations(positions, 2))
    for c in comb:
        antinodes = distance(c, lines)
        count.update(antinodes)
print(len(count))

#-----------part 2--------------------------------------

    
def distance2(pair, matrix):
    p1,p2 = pair
    vect1 = (p1[0]-p2[0], p1[1]-p2[1])
    vect2 = (-vect1[0], -vect1[1])
    a,b = matrix.shape
    i,j = 1,1
    valid = set()
    while  is_valid(p1[0] + vect1[0]*i, p1[1] + vect1[1]*i, a, b):
        valid.add((p1[0] + vect1[0]*i, p1[1] + vect1[1]*i))
        i+=1
    while is_valid(p2[0] + vect2[0]*j, p2[1] + vect2[1]*j, a, b):
        valid.add((p2[0] + vect2[0]*j, p2[1] + vect2[1]*j))
        j+=1
    return valid

count2 = set()
for symbol, positions in antennas_positions.items():
    comb = list(itertools.combinations(positions, 2))
    for c in comb:
        count2.update(c)
        antinodes = distance2(c, lines)
        count2.update(antinodes)
print(len(count2))