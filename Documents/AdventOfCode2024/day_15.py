f = open("day_15_input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]
break_index = lines.index("") 
warehouse = [list(x) for x in lines[:break_index]]
movements = "".join(lines[break_index+1:])
# -----------part 1--------------------------------------

xi, yi = 0, 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == "@":
            xi, yi = i, j

def moving(a, b, move):
    if move == '^':
        return a - 1, b
    elif move == '>':
        return a, b + 1
    elif move == 'v':
        return a + 1, b
    elif move == '<':
        return a, b - 1


x, y = xi, yi
next_x, next_y = x,y
for move in movements:
    next_x, next_y = moving(x, y, move)
    if warehouse[next_x][next_y] == '.':
        warehouse[x][y] = '.'
        warehouse[next_x][next_y] = '@'
        x,y = next_x, next_y
    elif warehouse[next_x][next_y] == 'O':
        movable = True
        n,m = x, y
        while warehouse[n][m] != '.':
            if warehouse[n][m] == '#':
                movable = False
                break
            n,m = moving(n, m, move)
        if not movable:
            continue
        if y != m:
            section_to_move = warehouse[x][min(y,m):max(y,m)+1]
            if move == '<':
                warehouse[x][min(y,m):max(y,m)+1] = section_to_move[1:] + section_to_move[:1]
            elif move == '>':
                warehouse[x][min(y,m):max(y,m)+1] = section_to_move[-1:] + section_to_move[:-1]
        else:
            section_to_move = [row[y] for row in warehouse[min(x,n):max(x,n)+1]]
            if move == 'v':
                section_to_move = section_to_move[-1:] + section_to_move[:-1]
            elif move == '^':
                section_to_move = section_to_move[1:] + [section_to_move[0]]
            for i in range(len(section_to_move)):
                warehouse[min(x,n) + i][y] = section_to_move[i]
        x, y = next_x, next_y
        
    else: #when it's a #
        continue
# for row in warehouse:
#     print(" ".join(row))

s = 0 
for i, row in enumerate(warehouse):
      for j, item in enumerate(row):
          if item == 'O':
            s+= i*100 + j
print(s)
# -----------part 2--------------------------------------
