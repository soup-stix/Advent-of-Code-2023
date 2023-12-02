#part 2
import re

with open("Advent of Code 2023\day_1.txt", "r") as f:
    lines = f.readlines()

    valid = {'one': '1',
             'two': '2',
             'three' : '3',
             'four' : '4',
             'five' : '5',
             'six' : '6',
             'seven' : '7',
             'eight' : '8',
             'nine' : '9'}

    pattern = "("
    pattern_r = "("
    for num in valid:
        pattern += num + "|"
        pattern_r += num[::-1] + "|"

    pattern += "\d)"
    pattern_r += "\d)"
    print(pattern_r)
    output = 0

    for line in lines:
        curr = ''
        matches = [re.findall(pattern, line)[0], re.findall(pattern_r, line[::-1])[0][::-1]]
        for match in matches:
            if match in valid:
                curr += valid[match]
            else:
                curr += match
        output += int(curr)

print(output)