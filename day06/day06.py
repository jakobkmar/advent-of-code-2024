import copy

with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file]

og_grid = [list(line) for line in lines]

def run_guard_simulation(grid):
    current_pos = None
    for i, line in enumerate(grid):
        if '^' in line:
            current_pos = (i, line.index('^'))
            break
    if current_pos == None:
        return None

    directions = [(0, 1), (1, 0), (0, -1)]
    direction = (-1, 0)

    visited = []
    turning_points = set()

    while True:
        visited.append(current_pos)
        next_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            return visited
        if (grid[next_pos[0]][next_pos[1]] == '#'):
            directions.append(direction)
            direction = directions.pop(0)
            turning_point = (current_pos, direction)
            if turning_point in turning_points:
                return False
            turning_points.add(turning_point)
            continue
        current_pos = next_pos

# part 1
og_visited = set(run_guard_simulation(og_grid))
print("positions visited by guard:", len(og_visited))

# part 2

print("checking all possible obstacles...")
loop_variant_counter = 0
for y in range(len(og_grid)):
    for x in range(len(og_grid[0])):
        if og_grid[y][x] == '#' or (y, x) not in og_visited:
            continue
        print("\rchecking pos", "y:", str(y).zfill(3), "x:", str(x).zfill(3), end="")
        grid_copy = copy.deepcopy(og_grid)
        grid_copy[y][x] = '#'
        result = run_guard_simulation(grid_copy)
        if result == False:
            loop_variant_counter += 1
print("\n", end="")

print("one obstacle leads to loop:", loop_variant_counter)
