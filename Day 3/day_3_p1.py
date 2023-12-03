#part 1
# def remove_newline(data):
#     return [row[:-1] if row[-1] == "\n" else row for row in data]


# with open("Advent of Code 2023\Day 3\day_3.txt", "r") as f:
#     # engine_schema = f.readlines()
#     engine_schema = f.readlines()

# total = 0
# final_schema = []

# for line in engine_schema:
#     final_schema.append(list(line))

# final_schema = remove_newline(final_schema)
# print(final_schema)
# POS = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

# for i in range(len(final_schema)):
#     for j in range(len(final_schema[i])):
#         if not final_schema[i][j].isalnum() and not final_schema[i][j] == ".":
#             # print(final_schema[i][j])
#             for x,y in POS:
#                 if 0<=(i+x)<len(final_schema) and 0<=(j+y)<len(final_schema[i]) and final_schema[i+x][j+y].isdigit():
#                     print(final_schema[i][j],final_schema[i+x][j+y])

#                     total+=int(final_schema[i+x][j+y])


# print(len(final_schema), len(final_schema[0]))

# print(total)

grid = open("Advent of Code 2023\Day 3\day_3.txt", "r").read().splitlines()
print(grid)
cs = set()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue
        for dr in range(r - 1, r + 2):
            for dc in range(c - 1, c + 2):
                if dr < 0 or dr >= len(grid) or dc < 0 or dc >= len(grid[dr]) or not grid[dr][dc].isdigit():
                    continue
                while dc > 0 and grid[dr][dc - 1].isdigit():
                    dc -= 1
                cs.add((dr, dc))

ns = []

for r, c in cs:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    ns.append(int(s))

print(sum(ns))
