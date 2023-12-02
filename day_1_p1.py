#part 1
with open("Advent of Code 2023\day_1.txt", "r") as f:
    lines = f.readlines()

total = 0

for line in lines:
    first_num = 0
    last_num = 0
    for i in line.strip():
        if not i.isalpha():
            first_num = int(i)
            break
    for i in line[::-1].strip():
        if not i.isalpha():
            last_num = int(i)
            break

    print(line, first_num, last_num)

    total += (first_num*10)+last_num

print(total)


