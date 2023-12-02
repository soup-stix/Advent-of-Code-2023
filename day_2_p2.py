#remove "game no: from text and all the ","
#part 2
with open("Advent of Code 2023\day_2.txt", "r") as f:
    games = f.readlines()

final_games = []
total = 0

for game in games:
    tries = game.strip().split("; ")
    temp = []
    for inst in tries:
        temp.append(inst.split(" "))

    final_games.append(temp)

for game in range(len(final_games)):
    max_blue, max_red, max_green = 0, 0, 0
    for inst in final_games[game]:
        for i in range(0,len(inst)-1,1):
            if inst[i+1] == "blue":
                max_blue = max(max_blue, int(inst[i]))
            if inst[i+1] == "red":
                max_red = max(max_red, int(inst[i]))
            if inst[i+1] == "green":
                max_green = max(max_green, int(inst[i]))
    # print(final_games[game], max_blue, max_red, max_green, game+1)
    if max_green == 0:
        max_green = 1
    if max_blue == 0:
        max_blue = 1
    if max_red == 0:
        max_red = 1
    total += (max_blue*max_red*max_green)

print(total)


