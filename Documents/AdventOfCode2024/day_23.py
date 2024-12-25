from collections import defaultdict

f = open('day_23_input.txt','r')
lines = f.readlines()
lines = [x.strip().split('-') for x in lines]

#-----------part 1--------------------------------------

dict = defaultdict(set)

for line in lines:
    dict[line[0]].add(line[1])
    dict[line[1]].add(line[0])

triangles = set()
for key, value in dict.items():
    for val in value:
        intersect = list(dict[val] & value)
        if intersect:
            for i in intersect:
                sorted_tri = sorted((key, val, i))
                triangles.add(tuple(sorted_tri))

print(triangles)
print(len(triangles))

name_t = set()
for tri in triangles:
    for computer in tri:
        if computer.startswith('t'):
            name_t.add(tri)

print(len(name_t))
#-----------part 2--------------------------------------

L = list(triangles)
previous = L[0]
for i in range(1, len(L)):
    print(previous, L[i])
    inter = set(previous) & set(L[i])
    print(inter)
    previous = L[i]
    