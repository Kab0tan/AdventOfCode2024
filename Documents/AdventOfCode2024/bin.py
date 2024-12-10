

def parse_disk_map_with_multidigit_ids(disk_map):
    result = []
    file_id = 0
    i = 0
    while i < len(disk_map):
        file_length = int(disk_map[i])
        i += 1
        free_space = int(disk_map[i]) if i < len(disk_map) else 0
        i += 1

        # Add file blocks (use formatted ID if multi-digit required)
        result.extend([f"{file_id}"] * file_length)
        file_id += 1

        # Add free space
        result.extend(['.'] * free_space)
    
    return ''.join(result)

# Multi-digit IDs example



def find_leftmost_gap(disk_map):
    """Find the leftmost '.' (gap) in the disk map."""
    for i, char in enumerate(disk_map):
        if char == '.':
            return i
    return -1

def find_rightmost_file_block(disk_map):
    """Find the rightmost non-gap, non-zero character in the disk map."""
    for i in range(len(disk_map) - 1, -1, -1):
        if disk_map[i] != '.':
            return i
    return -1

def simulate_moves(initial_disk_map):
    """Simulate moving file blocks from right to left."""
    results = [initial_disk_map]
    current_map = list(initial_disk_map)
    
    while True:
        # Find the leftmost gap and rightmost file block
        left_gap = find_leftmost_gap(current_map)
        right_block = find_rightmost_file_block(current_map)
        
        # If no gap or no file block is found, or if gap is to the right of the last block,
        # the process is complete
        if left_gap == -1 or right_block == -1 or left_gap > right_block:
            break
            
        # Move the block
        print(left_gap, right_block)
        current_map[left_gap] = current_map[right_block]
        current_map[right_block] = '.'
        
        # Add the current state to results
        results = (''.join(current_map))
    return results

# Test with the examples

example1 = "0..111....22222"
example2 = "00...111...2...333.44.5555.6666.777.888899"

f = open('day_9_input.txt','r')
lines = f.readlines()
final = parse_disk_map_with_multidigit_ids(lines[0])
print(len)
steps2 = simulate_moves(final)
s = 0 
for idx, item in enumerate(steps2):
    if item == '.':
        break
    s += idx*int(item)
print(s)
