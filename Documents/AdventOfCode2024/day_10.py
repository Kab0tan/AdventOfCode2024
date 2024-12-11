f = open('day_10_input.txt','r')
lines = f.readlines()
lines = [ list(x.strip()) for x in lines]

#-----------part 1--------------------------------------
def neighbors(i,j,a,b):
    n = []
    if i-1>=0:
        n.append((i-1,j))
    if i+1<a:
        n.append((i+1,j))
    if j-1>=0:
        n.append((i,j-1))
    if j+1<b:
        n.append((i,j+1))
    return n

def check_neighbors(i,j,a,b, visited, end):
    curr = lines[i][j]
    n = neighbors(i,j,a,b)
    for x in n:
        if int(lines[x[0]][x[1]]) == int(curr)+1 and x not in visited:
            visited.add(x)
            if lines[x[0]][x[1]] == '9':
                end[0]+=1
            check_neighbors(x[0],x[1],a,b,visited, end)
            


score = 0
for i, row in enumerate(lines):
    for j, item in enumerate(row):
        if item == '0':
            e = [0]
            check_neighbors(i,j,len(lines),len(lines[0]),{(i,j)}, e)
            score += e[0]
print(score)
#-----------part 2--------------------------------------

def check_neighbors2(i,j,a,b, rating):
    curr = lines[i][j]
    n = neighbors(i,j,a,b)
    for x in n:
        if int(lines[x[0]][x[1]]) == int(curr)+1:
            if lines[x[0]][x[1]] == '9':
                rating[0]+=1
            check_neighbors2(x[0],x[1],a,b, rating)
            
score = 0
for i, row in enumerate(lines):
    for j, item in enumerate(row):
        if item == '0':
            ratings = [0]
            check_neighbors2(i,j,len(lines),len(lines[0]), ratings)
            score += ratings[0]
print(score)