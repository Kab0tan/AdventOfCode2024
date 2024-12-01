f = open('day_1_input.txt','r')
lines = f.readlines()

lines = [ x.split() for x in lines]

#-----------part 1--------------------------------------

left = sorted([int(pair[0]) for pair in lines])
right = sorted([int(pair[1]) for pair in lines])

diff = [ abs(x - y) for x,y in zip(left, right)]

print(sum(diff))


#-----------part 2--------------------------------------

similarity_score = 0 

for element in left:
    similarity_score += element * right.count(element)
    
print(similarity_score)