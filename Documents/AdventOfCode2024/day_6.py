import numpy as np

f = open("day_6_input.txt", "r")
lines = f.readlines()
matrix = np.array([list(x.strip()) for x in lines])

a, b = matrix.shape
xi, yi = np.where(matrix == "^")[0][0], np.where(matrix == "^")[1][0]
directions = {
    "^": ((0, 1), ">"),
    ">": ((1, 0), "v"),
    "v": ((0, -1), "<"),
    "<": ((-1, 0), "^"),
}
x, y = xi, yi
dir = (-1, 0)
curr = "^"

# -----------part 1--------------------------------------
visited = {}
visited[(x, y)] = None
while (0 <= x + dir[0] < a) and (0 <= y + dir[1] < b):
    x, y = x + dir[0], y + dir[1]
    visited[(x, y)] = None
    if (
        (x + dir[0] == 0 or x + dir[0] == a - 1)
        or (y + dir[1] == b - 1 or y + dir[1] == 0)
    ) and matrix[x + dir[0], y + dir[1]] != "#":

        visited[(x + dir[0], y + dir[1])] = None
        break
    if matrix[x + dir[0], y + dir[1]] == "#":
        dir = directions[curr][0]
        curr = directions[curr][1]
visited = list(visited.keys())
# print(len(visited))
# print(visited)

# -----------part 2--------------------------------------


# def is_loop(init_x, init_y, M, curr_sign, curr_dir, loop_visited):
#     local_loop_visited = {(init_x, init_y)}
#     loop_x, loop_y = init_x, init_y
#     loop_dir = curr_dir
#     loop_current_sign = curr_sign
#     # print(loop_x, loop_y, loop_dir, curr_sign, loop_visited)
#     while True:
#     # for i in range(40):
#         next_position = (loop_x+loop_dir[0], loop_y+loop_dir[1])
#         # print(next_position, loop_dir, loop_current_sign, local_loop_visited)
#         # if next_position == (init_x, init_y) : #we are in a closed path
#         if next_position in loop_visited : #we are in a closed path
#             return True
#         if next_position in local_loop_visited:
#             loop_visited.add(next_position)
#             return is_loop(next_position[0], next_position[1], M, loop_current_sign, loop_dir, loop_visited)
#         if ((next_position[0] == 0 or next_position[0] == a-1) or (next_position[1] == b-1 or next_position[1] == 0)) and M[next_position[0],next_position[1]] != '#':
#             return False
#         if M[next_position[0],next_position[1]] == '#':
#             loop_dir = directions[loop_current_sign][0]
#             loop_current_sign = directions[loop_current_sign][1]
#         loop_x, loop_y = (loop_x+loop_dir[0], loop_y+loop_dir[1])
#         local_loop_visited.add((loop_x, loop_y))

# loop_count = 0
# for coor in visited:
#     i, j = coor
#     dir = (-1, 0)
#     curr = "^"
#     m = matrix.copy()
#     m[i, j] = "#"
#     visited2 = {(xi, yi)}
#     x, y = xi, yi
#     # while True:
#     #     x,y = x+dir[0], y+dir[1] #next position
#     #     if (x,y) in visited2:
#     #         if is_loop(x,y,m, curr, dir, {(x, y)}):
#     #             print(i,j)
#     #             loop_count += 1
#     #             break
#     #         else:
#     #             break
#     #     visited2.add((x,y))
#     #     if ((x+dir[0] == 0 or x+dir[0] == a-1) or (y+dir[1] == b-1 or y+dir[1] == 0)) and m[x+dir[0],y+dir[1]] != '#':
#     #         #we reach the border
#     #         break
#     #     if m[x+dir[0],y+dir[1]] == '#':
#     #         dir = directions[curr][0]
#     #         curr = directions[curr][1]
#     while True:
#         x, y = x + dir[0], y + dir[1]  # next position
#         if (x, y) in visited2 and m[x, y] == "+":
#             loop_count += 1
#             break
#         if (
#             (x + dir[0] == 0 or x + dir[0] == a - 1)
#             or (y + dir[1] == b - 1 or y + dir[1] == 0)
#         ) and m[x + dir[0], y + dir[1]] != "#":
#             # we reach the border
#             break
#         if m[x + dir[0], y + dir[1]] == "#":
#             dir = directions[curr][0]
#             curr = directions[curr][1]
#             m[x, y] = "+"
#         visited2.add((x, y))


def can_loop(right_view, arrow_symbol ):
    if arrow_symbol in right_view : #we are looking at the rigth, if there is a 0, it means on the right there is a point we already visited
        if '#' in right_view :
            index_hashtag = np.where(right_view == '#')[0][0]
            index_arrow = np.where(right_view == arrow_symbol)[0][0]
            if index_arrow < index_hashtag:
                return True
            return False
        return True
    return False

m = matrix.copy()
visited2 = {}
direction_pair = (-1,0)
curr_symbol = "^"
x, y = xi, yi
count_obstacles = 0
while (0 <= x + dir[0] < a) and (0 <= y + dir[1] < b):
    visited2[(x,y)] = None
    if curr_symbol == "^":
        m[x,y] = '^'
        #we are looking at the rigth, if there is a 0, it means on the right there is a point we already visited
        right_view = m[x,y:]
        if can_loop(m[x,y:], '>'):
            print("we can add an obstacle at ", x+1,y)
            count_obstacles += 1
    elif curr_symbol == ">":
        m[x,y] = '>'
        if can_loop(m[x:,y], 'v'):
            print("we can add an obstacle at ", x,y+1)
            count_obstacles += 1
    elif curr_symbol == "v":
        m[x,y] = 'v'
        if can_loop(m[x,:y][::-1], '<'):
            print("we can add an obstacle at ", x+1,y)
            count_obstacles += 1
    elif curr_symbol == "<":
        m[x,y] = '<'
        if can_loop(m[:x,y][::-1], '^'):
            print("we can add an obstacle at ", x,y-1)
            count_obstacles += 1
    if m[x+direction_pair[0],y+direction_pair[1]] == "#":
        direction_pair = directions[curr_symbol][0]
        curr_symbol = directions[curr_symbol][1]
    x, y = x + direction_pair[0], y + direction_pair[1]
print(count_obstacles)