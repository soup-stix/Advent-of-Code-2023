#remove "card no: from text
#part 1
with open("Advent of Code 2023\Day 4\day_4.txt", "r") as f:
    cards = f.readlines()

final_games = []
total = 0

for card in cards:
    winning, mine = card.split("|")
    # print(wining, mine)
    winning = set({x for x in winning.split(" ") if x != ''})
    # print(mine.split()) 
    temp = 0
    for num in mine.split():
        if num in winning:
            if temp == 0:
                temp = 1
            else:
                temp *= 2

    total += temp
    
print(total)


