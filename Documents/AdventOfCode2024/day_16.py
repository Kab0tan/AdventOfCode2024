from queue import PriorityQueue

f = open('day_16_input.txt','r')
lines = f.readlines()
lines = [list(x.strip()) for x in lines]


#-----------part 1--------------------------------------

directions = [ (0,1), (1,0), (0,-1), (-1,0) ]

pq = PriorityQueue()
S_pos = (len(lines)-2, 1)
E_pos = (1, len(lines[0])-2)
cost = 0
dir = (0,1)
pq.put((cost, S_pos, dir))
visited = set()
while pq:
    cost, pos, dir = pq.get()
    if pos == E_pos:
        print("lowest cost", cost)
        print("len", pq.qsize())
        break
    if pos in visited:
        continue
    visited.add(pos)
    for turn in [-1, 0, 1]:
        new_dir_index = (directions.index(dir) + turn) % 4
        new_dir = directions[new_dir_index]
        new_x, new_y = pos[0] + new_dir[0], pos[1] + new_dir[1]
        if lines[new_x][new_y] == '#':
            continue
        else:
            new_cost = cost
            if turn != 0:
                new_cost += 1000
            new_cost += 1
            pq.put((new_cost,(new_x, new_y), new_dir))

for vis in visited:
    lines[vis[0]][vis[1]] = 'O'
print(lines)

#-----------part 2--------------------------------------

# WIP: P2 code complexity too hig for real input

# directions = [ (0,1), (1,0), (0,-1), (-1,0) ]

# pq = PriorityQueue()
# S_pos = (len(lines)-2, 1)
# E_pos = (1, len(lines[0])-2)
# cost = 0
# dir = (0,1)
# local_visited = set()
# pq.put((cost, S_pos, dir, local_visited))
# best_paths = set()
# while not pq.empty():
#     cost, pos, dir, local_visited = pq.get()
#     if pos == E_pos:
#         print("lowest cost", cost)
#         best_paths.update(local_visited)
#         while not pq.empty():
#             threshold, pos, dir, local_visited = pq.get()
#             if threshold > cost or E_pos not in local_visited:
#                 break
#             best_paths.update(local_visited)
            
#         break
#     for turn in [-1, 0, 1]:
#         new_dir_index = (directions.index(dir) + turn) % 4
#         new_dir = directions[new_dir_index]
#         new_x, new_y = pos[0] + new_dir[0], pos[1] + new_dir[1]
#         if lines[new_x][new_y] == '#':
#             continue
#         else:
#             new_local_visited = local_visited.copy()
#             new_cost = cost
#             if turn != 0:
#                 new_cost += 1000
#             new_cost += 1
#             new_local_visited.add((new_x, new_y))
#             pq.put((new_cost,(new_x, new_y), new_dir, new_local_visited))

# print(len(best_paths)+1)
# print(E_pos, S_pos)