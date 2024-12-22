from queue import Queue


f = open('day_20_input.txt','r')
lines = f.readlines()
maze = [ list(x.strip()) for x in lines]

#-----------part 1--------------------------------------


directions = [ (0,1), (1,0), (0,-1), (-1,0) ]

S_pos = (0,0)
E_pos = (0,0)
for row in maze: 
    if 'S' in row:
        S_pos = (maze.index(row),row.index('S'))
    if 'E' in row:
        E_pos = ( maze.index(row), row.index('E'))

# BFS function to find the shortest path
def bfs_maze(maze, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    visited = set()
    queue = Queue()
    queue.put((start, 0))  # (position, steps)
    visited.add(start)

    while not queue.empty():
        position, steps = queue.get()
        if position == end:
            return steps

        for direction in directions:
            new_x, new_y = position[0] + direction[0], position[1] + direction[1]
            new_position = (new_x, new_y)

            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                maze[new_x][new_y] != '#' and new_position not in visited):
                queue.put((new_position, steps + 1))
                visited.add(new_position)

    return -1  # If no path is found

max_step = bfs_maze(maze, S_pos, E_pos)
savings = {}
print(max_step)
step = 0
previous = S_pos
while S_pos != E_pos:
# for i in range(20):
    if S_pos == E_pos:
        step = step + 1
        break
    next_point = None
    for direction in directions:
        new_x, new_y = S_pos[0] + direction[0], S_pos[1] + direction[1]
        if new_x < 0 or new_x >= len(maze) or new_y < 0 or new_y >= len(maze) or (new_x, new_y) == previous:
            continue
        elif maze[new_x][new_y] == '#':
            next_next_point = new_x+direction[0], new_y+direction[1]
            if next_next_point[0] > 0 and next_next_point[0] < len(maze) and next_next_point[1] > 0 and next_next_point[1] < len(maze) and maze[next_next_point[0]][next_next_point[1]] != '#':
                end_step = bfs_maze(maze, (new_x+direction[0], new_y+direction[1]), E_pos)
                end_step += 2
                save = max_step - (step + end_step)
                savings.setdefault(save, 0)  # Initialize the key with 0 if it doesn't exist
                savings[save] += 1
        else:
            next_point = (new_x, new_y)
    previous = S_pos
    step = step + 1
    S_pos = next_point
print(savings)
print(sum(value for key, value in savings.items() if key >= 100))


#-----------part 2--------------------------------------