def parse_input(line):
    """
    Parse the input line to create file and disk stacks.
    """
    file_stack = []
    disk_stack = []
    count_file = 0
    is_file = True  # Alternates between file count and disk spaces

    for i, char in enumerate(line):
        count = int(char)
        if is_file:
            # Add file IDs to the file stack
            for _ in range(count):
                file_stack.append(i // 2)  # File ID corresponds to position in input
            count_file += count
        else:
            # Add disk count to the disk stack
            disk_stack.append(count)
        is_file = not is_file

    return file_stack, disk_stack


def compute_final_disk(file_stack, disk_stack):
    """
    Build the final disk layout by arranging files and disks.
    """
    final_disk = []
    i_start_files = 0
    i_end_files = len(file_stack) - 1
    start_file_id = file_stack[i_start_files] if file_stack else None

    for i in range(len(disk_stack) * 2):  # Each disk stack has a corresponding file section
        if i % 2:  # Odd index: fill with disk spaces
            for _ in range(disk_stack[i // 2]):
                if i_end_files >= i_start_files:
                    final_disk.append(file_stack[i_end_files])
                    i_end_files -= 1
        else:  # Even index: fill with files
            while (
                i_start_files <= i_end_files
                and file_stack[i_start_files] == start_file_id
            ):
                final_disk.append(file_stack[i_start_files])
                i_start_files += 1
            start_file_id = (
                file_stack[i_start_files]
                if i_start_files <= i_end_files
                else None
            )

    return final_disk


def compute_score(final_disk):
    """
    Compute the score for the final disk arrangement.
    """
    score = 0
    for i, file_id in enumerate(final_disk):
        score += i * file_id
    return score


# Input and execution
f = open('day_9_input.txt','r')
lines = f.readlines()
file_stack, disk_stack = parse_input(lines[0])
final_disk = compute_final_disk(file_stack, disk_stack)
score = compute_score(final_disk)

print(f"Final Disk: {final_disk}")
print(f"Score: {score}")
