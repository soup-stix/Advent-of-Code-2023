#remove "game no: from text and all the ","
#part 1
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
    flag = 1
    for inst in final_games[game]:
        for i in range(0,len(inst)-1,1):
            if inst[i+1] == "blue" and int(inst[i]) > 14:
                flag = 0
            if inst[i+1] == "red" and int(inst[i]) > 12:
                flag = 0
            if inst[i+1] == "green" and int(inst[i]) > 13:
                flag = 0
    # print(final_games[game], flag, game+1)
    if flag == 1:
        total += (game+1)

    
print(total)


