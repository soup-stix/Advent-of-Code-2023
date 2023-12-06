# #remove "card no: from text
# #part 2
with open("Advent of Code 2023\Day 4\day_4.txt", "r") as f:
    cards = f.readlines()

all_cards = {}

for card in range(len(cards)):
    winning, mine = cards[card].split("|")
    # print(wining, mine)
    winning = set({x for x in winning.split(" ") if x != ''})
    # print(mine.split()) 
    temp = 0
    if card not in all_cards:
        all_cards[card] = 1
    else:
        all_cards[card] = 1 + all_cards[card]

    for num in mine.split():
        if num in winning:
            temp += 1

    # print(temp)
    
    for i in range(1,temp+1):
        if (card+i) not in all_cards:
            all_cards[(i+card)] = 1
        else:
            all_cards[(i+card)] = all_cards[(i+card)] + all_cards[(card)] 
    # print(card+i, all_cards)
    # print("next")

# print(all_cards)
print(sum(all_cards.values()))
