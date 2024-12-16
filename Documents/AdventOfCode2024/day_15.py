f = open("day_15_input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]
break_index = lines.index("") 
warehouse = [list(x) for x in lines[:break_index]]
movements = "".join(lines[break_index+1:])
# -----------part 1--------------------------------------

# xi, yi = 0, 0
# for i in range(len(warehouse)):
#     for j in range(len(warehouse[i])):
#         if warehouse[i][j] == "@":
#             xi, yi = i, j

# def moving(a, b, move):
#     if move == '^':
#         return a - 1, b
#     elif move == '>':
#         return a, b + 1
#     elif move == 'v':
#         return a + 1, b
#     elif move == '<':
#         return a, b - 1


# x, y = xi, yi
# next_x, next_y = x,y
# for move in movements:
#     next_x, next_y = moving(x, y, move)
#     if warehouse[next_x][next_y] == '.':
#         warehouse[x][y] = '.'
#         warehouse[next_x][next_y] = '@'
#         x,y = next_x, next_y
#     elif warehouse[next_x][next_y] == 'O':
#         movable = True
#         n,m = x, y
#         while warehouse[n][m] != '.':
#             if warehouse[n][m] == '#':
#                 movable = False
#                 break
#             n,m = moving(n, m, move)
#         if not movable:
#             continue
#         if y != m:
#             section_to_move = warehouse[x][min(y,m):max(y,m)+1]
#             if move == '<':
#                 warehouse[x][min(y,m):max(y,m)+1] = section_to_move[1:] + section_to_move[:1]
#             elif move == '>':
#                 warehouse[x][min(y,m):max(y,m)+1] = section_to_move[-1:] + section_to_move[:-1]
#         else:
#             section_to_move = [row[y] for row in warehouse[min(x,n):max(x,n)+1]]
#             if move == 'v':
#                 section_to_move = section_to_move[-1:] + section_to_move[:-1]
#             elif move == '^':
#                 section_to_move = section_to_move[1:] + [section_to_move[0]]
#             for i in range(len(section_to_move)):
#                 warehouse[min(x,n) + i][y] = section_to_move[i]
#         x, y = next_x, next_y
        
#     else: #when it's a #
#         continue
# # for row in warehouse:
# #     print(" ".join(row))

# s = 0 
# for i, row in enumerate(warehouse):
#       for j, item in enumerate(row):
#           if item == 'O':
#             s+= i*100 + j
# print(s)


# -----------part 2--------------------------------------

warehouse2 = []
for row in warehouse:
    row2 = []
    for cell in row:
        if cell == ".":
            row2+= ["."]*2
        elif cell == "#":
            row2+= ["#"]*2
        elif cell == "O":
            row2+= ["["] + ["]"]
        else:
            row2+= ["@"] + ["."]
    warehouse2.append(row2)


xi, yi = 0, 0
for i in range(len(warehouse2)):
    for j in range(len(warehouse2[i])):
        if warehouse2[i][j] == "@":
            xi, yi = i, j
print(xi, yi)

def moving(a, b, move):
    if move == '^':
        return a - 1, b
    elif move == '>':
        return a, b + 1
    elif move == 'v':
        return a + 1, b
    elif move == '<':
        return a, b - 1
    
    
def moving2(a, b, move, boxes, movable):
    local = []
    if warehouse2[a][b] == '[':
        boxes.setdefault(a, set()).update([(a,b), (a,b+1)])
        local.append((a,b))
        local.append((a,b+1))
    elif warehouse2[a][b] == ']':
        boxes.setdefault(a, set()).update([(a,b), (a,b-1)])
        local.append((a,b))
        local.append((a,b-1))
    elif warehouse2[a][b] == '#':
        movable[0] = False
    for box in local:
        a,b = moving(box[0], box[1], move)
        moving2(a,b, move, boxes, movable)
    
x, y = xi, yi
next_x, next_y = x,y
for index, move in enumerate(movements):
    next_x, next_y = moving(x, y, move)
    if warehouse2[next_x][next_y] == '.':
        warehouse2[x][y] = '.'
        warehouse2[next_x][next_y] = '@'
        x,y = next_x, next_y
    elif warehouse2[next_x][next_y] == '[' or warehouse2[next_x][next_y] == ']':
        movable = [True]
        n,m = next_x, next_y
        if move in ['>', '<']:
            while warehouse2[n][m] != '.':
                if warehouse2[n][m] == '#':
                    movable[0] = False
                    break
                n,m = moving(n, m, move)
            if not movable[0]:
                continue
            section_to_move = warehouse2[x][min(y,m):max(y,m)+1]
            if move == '<':
                warehouse2[x][min(y,m):max(y,m)+1] = section_to_move[1:] + section_to_move[:1]
            elif move == '>':
                warehouse2[x][min(y,m):max(y,m)+1] = section_to_move[-1:] + section_to_move[:-1]
        else:
            boxes_to_move = {}
            boxes_to_move.setdefault(x, []).extend([(x,y)])
            moving2(n, m, move, boxes_to_move, movable)
            if movable[0]:
                if move == '^':
                    for row_index in sorted(boxes_to_move):
                        for coor in boxes_to_move[row_index]:
                            warehouse2[coor[0]-1][coor[1]] = warehouse2[coor[0]][coor[1]]
                            warehouse2[coor[0]][coor[1]] = '.'
                elif move == 'v':
                    for row_index in sorted(boxes_to_move, reverse=True):
                        for coor in boxes_to_move[row_index]:
                            warehouse2[coor[0]+1][coor[1]] = warehouse2[coor[0]][coor[1]]
                            warehouse2[coor[0]][coor[1]] = '.'
            else:
                continue
        x, y = next_x, next_y

s = 0 
for i, row in enumerate(warehouse2):
      for j, item in enumerate(row):
          if item == '[':
            s+= i*100 + j
print(s)