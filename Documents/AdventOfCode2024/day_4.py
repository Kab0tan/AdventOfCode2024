import numpy as np

f = open('day_4_input.txt','r')
lines = f.readlines()
lines = np.array([list( x.strip()) for x in lines])

#-----------part 1--------------------------------------

def diag(a,b, word, lines, dir):
    L = len(word)
    if dir == 'SE':
        n, m = 1,1
    elif dir == 'NE':
        n, m = -1, 1
    elif dir == 'SW':
        n, m = 1, -1
    elif dir == 'NW':
        n, m = -1, -1
    return np.array([lines[a+(t*n),b+(t*m)] for t in range(L)])


word = np.array(list('XMAS'))
count = 0
x,y = lines.shape
for i in range(x):
    for j in range(y):
        if lines[i,j] == word[0]:
            #Check both horizontal
            #right
            if j+len(word)<= y and (lines[i,j:j+len(word)] == word).all():
                count += 1
            #left
            if j-len(word)+1>= 0 and (lines[i,j-len(word)+1:j+1] == word[::-1]).all():
                count += 1
            #Check both vertical
            #down
            if i+len(word)<= x and (lines[i:i+len(word),j] == word).all():
                count += 1
            #up
            if i-len(word)+1>= 0 and (lines[i-len(word)+1:i+1,j] == word[::-1]).all():
                count += 1
            #Check both diagonal
            #SE
            if i+len(word)<= x and j+len(word) <= y and (diag(i,j,word,lines,'SE') == word).all():
                count += 1
            #SW
            if i+len(word)<= x and j-len(word)+1 >= 0 and (diag(i,j,word,lines,'SW') == word).all():
                count += 1
            #NE
            if i-len(word)+1>= 0 and j+len(word) <= y and (diag(i,j,word,lines,'NE') == word).all():
                count += 1
            #NW
            if i-len(word)+1>= 0 and j-len(word)+1 >= 0 and (diag(i,j,word,lines,'NW') == word).all():
                count += 1
print(count)
#-----------part 2--------------------------------------

patterns = [np.array([['S',0,'S'],
                     [0,'A',0],
                     ['M',0,'M']]),
            np.array([['M',0,'M'],
                     [0,'A',0],
                     ['S',0,'S']]),
            np.array([['S',0,'M'],
                     [0,'A',0],
                     ['S',0,'M']]),
            np.array([['M',0,'S'],
                     [0,'A',0],
                     ['M',0,'S']]),
            ]

def is_valid(matrix, patterns):
    m = matrix.copy()
    m[0,1] = 0
    m[1,0] = 0
    m[1,2] = 0
    m[2,1] = 0
    return any(np.array_equal(m, pattern) for pattern in patterns)

count2 = 0
for i in range(x):
    for j in range(y):
        if lines[i,j] == 'A' and i-1>=0 and i+1<x and j+1<y and j-1>=0:
            if is_valid(lines[i-1:i+2,j-1:j+2], patterns):
                count2+=1 
print(count2)