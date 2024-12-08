with open("input.txt", "r") as input_file:
    grid = [line.strip() for line in input_file]

frequencies = set("".join(grid)) - set(".")

antinodes = []

for freq in frequencies:
    # read antenna positions for this frequency from the grid
    antennas = []
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == freq:
                antennas.append((x, y))

    # calculate antinodes for each pair of antennas
    pairs = [(a, b) for a in antennas for b in antennas if a != b]
    for pair in pairs:
        a, b = pair
        vector = (b[0] - a[0], b[1] - a[1])
        loop_count = 0 # part 2, for part 1 remove the loop
        while True:
            antinode = (a[0] - loop_count * vector[0], a[1] - loop_count * vector[1])
            if 0 <= antinode[0] < len(grid[0]) and 0 <= antinode[1] < len(grid):
                antinodes.append(antinode)
            else:
                break
            loop_count += 1

print(f"Number of antinodes: {len(set(antinodes))}")
