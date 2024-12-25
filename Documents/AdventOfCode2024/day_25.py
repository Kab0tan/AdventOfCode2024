f = open('day_25_input.txt','r')
lines = f.read()
lines = [line.split() for line in lines.strip().split('\n\n')]

def convert_to_height(matrix):
    return [ column.count('#')-1 for column in zip(*matrix) ]

def is_overlapping(key, lock):
    return not all( K + L < 6 for K, L in zip(key, lock))

locks = []
keys = []
for matrix in lines:
    if all( x =="#" for x in matrix[0]):
        locks.append(convert_to_height(matrix))
    else:
        keys.append(convert_to_height(matrix))
        

#-----------part 1--------------------------------------

count = 0
for keyM in keys:
    for lockM in locks:
        if not is_overlapping(keyM, lockM):
            count += 1

print(count)


#-----------part 2--------------------------------------