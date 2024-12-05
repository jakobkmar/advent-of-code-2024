with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file]

grid = [list(line) for line in lines]
word = "XMAS"

directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
rows = len(grid)
cols = len(grid[0])

def search_word(word, grid, directions):
    count = 0
    for i in range(rows):
        for j in range(cols):
            for direction in directions:
                dx, dy = direction
                x, y = i, j
                found = True
                for letter in word:
                    if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != letter:
                        found = False
                        break
                    x += dx
                    y += dy
                if found:
                    count += 1
    return count

count = search_word(word, grid, directions)

print(count)

# part 2

grid_copy = [list(line) for line in lines]
for i in range(rows):
    for j in range(cols):
        if grid_copy[i][j] != ".":
            grid_copy[i][j] = "."

def search_mas(grid):
    # do this by going through the grid and checking if the letter is an A
    # if yes, check if the letters around it form a MAS pattern diagonally
    # if yes, yield the index of the A letter
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "A":
                tl_br_satisfied = False
                tr_bl_satisfied = False
                # check diagonal from top left to bottom right
                try:
                    if i - 1 < 0 or j - 1 < 0:
                        pass
                    elif grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S":
                            tl_br_satisfied = True
                    elif grid[i + 1][j + 1] == "M" and grid[i - 1][j - 1] == "S":
                            tl_br_satisfied = True
                except IndexError:
                    pass
                # check diagonal from top right to bottom left
                try:
                    if i - 1 < 0 or j - 1 < 0:
                        pass
                    elif grid[i + 1][j - 1] == "M" and grid[i - 1][j + 1] == "S":
                        tr_bl_satisfied = True
                    elif grid[i - 1][j + 1] == "M" and grid[i + 1][j - 1] == "S":
                        tr_bl_satisfied = True
                except IndexError:
                    pass
                if tl_br_satisfied and tr_bl_satisfied:
                    # add all letters from this X to the grid_copy
                    grid_copy[i][j] = grid[i][j]
                    grid_copy[i - 1][j - 1] = grid[i - 1][j - 1]
                    grid_copy[i + 1][j + 1] = grid[i + 1][j + 1]
                    grid_copy[i + 1][j - 1] = grid[i + 1][j - 1]
                    grid_copy[i - 1][j + 1] = grid[i - 1][j + 1]
                    yield (i, j)

mas_indices = list(search_mas(grid))
print(mas_indices)

for row in grid_copy:
    print("".join(row))

print(len(mas_indices))
