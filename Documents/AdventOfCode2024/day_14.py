import numpy as np
import math
import matplotlib.pyplot as plt 

f = open('day_14_input.txt','r')
lines = f.readlines()
lines = [x.strip().split(' ') for x in lines]

width, height = 101, 103

# dict = {'TL':0, 'TR':0, 'BL':0, 'BR':0}
# for line in lines:
#     robot_pos = line[0].split('=')[1].split(',')
#     velocity = line[1].split('=')[1].split(',')
#     x, y = int(robot_pos[0]), int(robot_pos[1])
#     v = int(velocity[0]), int(velocity[1])
#     for i in range(100):
#         new_x = x+v[0]
#         new_y = y+v[1]
#         if new_x < 0 or new_x >= width:
#             new_x = abs(abs(new_x)-width)
#         if new_y < 0 or new_y >= height:
#             new_y = abs(abs(new_y)-height)
#         x, y = new_x, new_y
#     if x < width//2 and y < height//2:
#         dict['TL'] += 1
#     elif x < width//2 and y > height//2:
#         dict['BL'] += 1
#     elif x > width//2 and y < height//2:
#         dict['TR'] += 1
#     elif x > width//2 and y > height//2:
#         dict['BR'] += 1
        
# print(math.prod(dict.values()))
#-----------part 1--------------------------------------


M = np.zeros((width, height))
# Parse initial positions and velocities
positions = []
velocities = []

for line in lines:
    robot_pos = line[0].split('=')[1].split(',')
    velocity = line[1].split('=')[1].split(',')
    positions.append([int(robot_pos[0]), int(robot_pos[1])])
    velocities.append((int(velocity[0]), int(velocity[1])))

# Prepare the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()

# Loop for 10 iterations
for i in range(200):
    # Update positions for each robot
    for idx, (pos, vel) in enumerate(zip(positions, velocities)):
        x, y = pos
        v_x, v_y = vel

        # Reset the current position in the matrix (optional)
        M[x, y] = 0  

        # Calculate the new position
        new_x = x + v_x
        new_y = y + v_y

        # Handle wrapping or boundary conditions
        if new_x < 0 or new_x >= width:
            new_x = abs(abs(new_x) - width)
        if new_y < 0 or new_y >= height:
            new_y = abs(abs(new_y) - height)

        # Update the position
        positions[idx] = [new_x, new_y]

        # Mark the new position in the matrix
        M[new_x, new_y] += 1

    # Plot the matrix at this step
    ax.clear()
    ax.imshow(M, cmap='viridis')
    ax.set_title(f"Iteration {i+1}")
    plt.pause(0.5)  # Pause to visualize each step

plt.ioff()  # Turn off interactive mode
plt.show()  # Final display

#-----------part 2--------------------------------------