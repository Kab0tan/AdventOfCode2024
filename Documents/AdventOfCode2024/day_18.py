from queue import PriorityQueue

f = open('day_18_input.txt','r')
lines = f.readlines()



#-----------part 1--------------------------------------

def create_map(nb_bytes, shape):
    M = [['.']*shape for i in range(shape)]
    for line in lines[:nb_bytes]:
        x,y = int(line.strip().split(',')[0]), int(line.strip().split(',')[1])
        M[y][x] = '#'
    return M

def a_star(nb_bytes, size):
    M = create_map(nb_bytes, size)
    directions = [ (0,1), (1,0), (0,-1), (-1,0) ]
    pq = PriorityQueue()
    S_pos = (0, 0)
    E_pos = (len(M)-1, len(M)-1)
    cost = 0
    step = 0
    pq.put((step, cost, S_pos))
    visited = set()
    path_found = False

    while not pq.empty():
        step, cost, pos = pq.get()
        if pos == E_pos:
            path_found = True
            break
        if pos in visited:
            continue
        visited.add(pos)
        for direction in directions:
            new_x, new_y = pos[0] + direction[0], pos[1] + direction[1]
            if new_x < 0 or new_x >= len(M) or new_y < 0 or new_y >= len(M) or M[new_x][new_y] == '#':
                continue
            else:
                manhattan = abs(new_x - E_pos[0]) + abs(new_y - E_pos[1])
                new_step = step + 1
                new_cost = 1 + manhattan + cost
                pq.put((new_step, new_cost,(new_x, new_y)))
    return step, path_found
                
lowest_step, path_found = a_star(1024, 71)
print(lowest_step)
#-----------part 2--------------------------------------

for nb_bytes in range(len(lines)):
    lowest_step, path_found = a_star(nb_bytes, 71)

    if not path_found:
        print("no path found at", nb_bytes)
        break