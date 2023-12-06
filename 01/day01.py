# AoC 2023 Day1
# spiikki / nalleperhe
#
# find first and last numerical (int) values from each row, combine and sum up all combined values

final_sum = int()

search_table = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]

def findFirst(source, table):
    result = []
    for target in table:
        result.append(source.find(target))
    index = 666
    position = -1
    for i, value in enumerate(result):
        if value > -1:
            if value < index:
                index = value
                position = i
    if position+1 == 18 or position+1 == 9:
        return 9
    else:
        return (position+1)%9

def findLast(source, table):
    result = []
    for target in table:
        result.append(source.rfind(target))
    index = -1
    position = -1
    for i, value in enumerate(result):
        if value > -1:
            if value > index:

                index = value
                position = i
    if position+1 == 18 or position+1 == 9:
        return 9
    else:
        return (position+1)%9


with open('data') as data:
    for line in data:
        print(line)
        f = findFirst(line, search_table)
        l = findLast(line, search_table)
        print(f"f: {f}, l: {l}")
        final_sum += int(str(f)+str(l))

print(final_sum)