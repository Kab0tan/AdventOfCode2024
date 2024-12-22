# WIP

from collections import deque
import itertools

f = open('day_21_input.txt','r')
lines = f.readlines()
codes = [x.strip() for x in lines]


numeric_keypad = [
    [7,8,9],
    [4,5,6],
    [1,2,3],
    ['',0,'A']
]

num_dict = {
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),
    '0': (3,1),
    'A': (3,2)
}

direc_keypad = [
    ['','^','A'],
    ['<','v','>'],
]

direc_dict = {
    '^': (0,1),
    'v': (1,1),
    '<': (1,0),
    '>': (1,2),
    'A': (0,2)
}

directions = {
    '^': (-1,0),
    'v': (1,0),
    '<': (0,-1),
    '>': (0,1)
}
#-----------part 1--------------------------------------


def sequence(ref_dict, sequence, current_point, true_grid):
    temp =[]
    for char in sequence:
        target = ref_dict[char]
        queue = deque([(current_point, '')])
        paths_symbol = []
        shortest_length = float('inf')
        while queue:
            node, symbols = queue.popleft()
            # Get the current position of the node
            x, y = node
            # If path exceeds shortest known length, we can stop
            if len(symbols) > shortest_length:
                continue
            # If target is reached
            if node == target:
                if len(symbols) < shortest_length:
                    shortest_length = len(symbols)
                    paths_symbol = [symbols]
                elif len(symbols) == shortest_length:
                    paths_symbol.append(symbols)
                continue

            # Explore all possible moves (up, down, left, right)
            for direction in directions:
                dx, dy = directions[direction]
                new_x, new_y = x + dx, y + dy
                # Check if the new position is within bounds
                if 0 <= new_x < len(true_grid) and 0 <= new_y < len(true_grid[0]) and true_grid[new_x][new_y] != '':
                    # Get the value of the new position on the keypad
                    if numeric_keypad[new_x][new_y] != '':  # Make sure the position is valid
                        new_node = (new_x, new_y)
                        # Add the new position to the queue
                        if new_node not in node:  # Avoid revisiting nodes in the same path
                            queue.append((new_node, symbols + direction))
        if len(paths_symbol) > 1:
            temp.append([x+'A' for x in paths_symbol])
        temp.append(paths_symbol[0]+'A')
        current_point = target
    return temp

def combinations(sequence):
    combinations = {0: ''}
    for item in sequence:
        new_combinations = {}
        for key, value in combinations.items():
            if isinstance(item, list):
                for index, subitem in enumerate(item):
                    new_combinations[index] = value + subitem
            else:
                new_combinations[key] = value + item
        combinations = new_combinations

    return list(combinations.values())


def find_shortest_sequence(input_sequence, direc_dict, direc_keypad, position):
    """Find the shortest sequence within a given input sequence."""
    min_length = float('inf')
    best_sequence = None

    for seq in input_sequence:
        third_sequence = sequence(direc_dict, seq, position, direc_keypad)
        if len(third_sequence) < min_length:
            min_length = len(third_sequence)
            best_sequence = seq

    return best_sequence, min_length


def calculate_total_length(sequences, direc_dict, direc_keypad, position):
    """Calculate the total length of sequences, accounting for nested lists."""
    total_length = 0

    for seq in sequences:
        if isinstance(seq, list):
            best_seq, shortest_length = find_shortest_sequence(seq, direc_dict, direc_keypad, position)
            print(f"Shortest in nested sequence: {best_seq} with length {shortest_length}")
            total_length += shortest_length
        else:
            print("seq: ", seq)
            third_sequence = sequence(direc_dict, seq, position, direc_keypad)
            total_length += len(third_sequence)
            print(f"Third sequence: {third_sequence}")

    return total_length


# first_sequence = sequence(num_dict, codes[4], (3, 2), numeric_keypad)
# print(first_sequence)

# for seq in first_sequence:
#     if isinstance(seq, list):
#         shortest_seq, shortest_length = None, float('inf')

#         for s_seq in seq:
#             second_sequence = sequence(direc_dict, s_seq, (0, 2), direc_keypad)
#             print(f"\nSecond sequence: {second_sequence}")

#             total_length = calculate_total_length(second_sequence, direc_dict, direc_keypad, (0, 2))
#             print(f"Total length: {total_length}")

#             if total_length < shortest_length:
#                 shortest_length = total_length
#                 shortest_seq = s_seq

#         print(f"Shortest in first sequence: {shortest_seq} with length {shortest_length}")

#     else:
#         second_sequence_bis = sequence(direc_dict, seq, (0, 2), direc_keypad)
#         print(f"Second sequence (non-nested): {second_sequence_bis} for {seq}")

#         total_length_bis = calculate_total_length(second_sequence_bis, direc_dict, direc_keypad, (0, 2))
#         print(f"Total length (non-nested): {total_length_bis}")

  
  
  
print(sequence(direc_dict, '<A', (0, 2), direc_keypad))  
#-------------------------------------


# def sequence(ref_dict, sequence, current_point, true_grid):
#     final_sequence = []
#     previous_direction = None
#     for char in sequence:
#         target_pos = ref_dict[char]
#         while current_point != target_pos:
#             max = (999, None, None)
#             for direction in directions:
#                 dir_coor = directions[direction]
#                 next_point = (current_point[0] + dir_coor[0], current_point[1] + dir_coor[1])
#                 if next_point[0] < 0 or next_point[0] >= len(true_grid) or next_point[1] < 0 or next_point[1] >= len(true_grid[0]):
#                     continue
#                 else:
#                     if true_grid[next_point[0]][next_point[1]] == '':
#                         continue
#                     manhattan = abs(target_pos[0] - next_point[0]) + abs(target_pos[1] - next_point[1])
#                     penalty = 0 if direction == previous_direction else 1
#                     manhattan += penalty
#                     if manhattan < max[0]:
#                         max = (manhattan, next_point, direction)
#             current_point = max[1]
#             previous_direction = max[2]
#             final_sequence.append(max[2])
#         final_sequence.append('A')
#     return final_sequence


# score = 0
# for code in codes: 
#     first_sequence = sequence(num_dict, code, (3,2), numeric_keypad)
#     second_sequence = sequence(direc_dict, first_sequence, (0,2), direc_keypad)
#     third_sequence = sequence(direc_dict, second_sequence, (0,2), direc_keypad)
#     print(''.join(first_sequence))
#     print(''.join(second_sequence))
#     print(''.join(third_sequence))

#     length = len(third_sequence)
#     numeric = int(code[:-1])
#     print(length, numeric)
#     score += numeric * length

# print(score)

#problem, not always the shortest even with penalty
#-----------part 2--------------------------------------