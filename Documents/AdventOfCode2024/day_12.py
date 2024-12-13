f = open('day_12_input.txt','r')
lines = f.readlines()
lines = [x.strip() for x in lines]

#-----------part 1--------------------------------------

# def flood_fill(i,j,a,b, global_visited, local_visited, area, perimeter):
#     local_visited.add((i,j))
#     global_visited.add((i,j))
#     area[0] += 1
#     curr = lines[i][j]
#     for x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#         nx, ny = i+x[0], j+x[1]
#         if nx>=0 and nx<a and ny>=0 and ny<b:
#             if lines[nx][ny] == curr and (nx,ny) not in local_visited:
#                 flood_fill(nx, ny ,a ,b ,global_visited, local_visited, area, perimeter)
#             elif lines[nx][ny] != curr and (nx,ny) not in local_visited:
#                 perimeter[0]+=1
#         else:
#             perimeter[0] += 1
#     return

# score = 0
# GLOBAL_VISITED = set()
# for i, row in enumerate(lines):
#     for j in range(len(row)):
#         if (i,j) not in GLOBAL_VISITED:
#             LOCAL_VISITED = set()
#             area = [0]
#             perimeter = [0]
#             flood_fill(i,j,len(lines),len(lines[0]),GLOBAL_VISITED, LOCAL_VISITED, area, perimeter)
#             score += area[0] * perimeter[0]
# print(score)

#-----------part 2--------------------------------------

def flood_fill(i,j,a,b, global_visited, local_visited, area, local_sides):
    local_visited.add((i,j))
    global_visited.add((i,j))
    area[0] += 1
    curr = lines[i][j]
    print(i,j)
    for x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = i+x[0], j+x[1]
        if nx>=0 and nx<a and ny>=0 and ny<b:
            if lines[nx][ny] == curr and (nx,ny) not in local_visited:
                flood_fill(nx, ny ,a ,b ,global_visited, local_visited, area, local_sides)
            elif lines[nx][ny] != curr and (nx,ny) not in local_visited:
                if x[0] == 0:
                    local_sides['col'].append(ny)
                if x[1] == 0:
                    local_sides['row'].append(nx)
        else:
            if x[0] == 0:
                local_sides['col'].append(ny)
            if x[1] == 0:
                local_sides['row'].append(nx)
    return

score = 0
GLOBAL_VISITED = set()
for i, row in enumerate(lines):
    for j in range(len(row)):
        if (i,j) not in GLOBAL_VISITED:
            LOCAL_VISITED = set()
            area = [0]
            perimeter = [0]
            local_sides = {'row': [], 'col': []}
            flood_fill(i,j,len(lines),len(lines[0]),GLOBAL_VISITED, LOCAL_VISITED, area, local_sides)
            print(local_sides)
print(score)