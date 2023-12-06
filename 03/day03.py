# AoC 2023 / Day 3 
# spiikki / nalleperhe
#
# find part numbers from map with adjacent symbols (other than . and numbers)

# helper function to return true/false if number has adjacent symbols next to it
def check_for_adjacent(map, number, gear_map, gear_sum_map):
    is_adjacent = False

    if number["start"]["x"] == 0:
        x_min_limit = 0
    else:
        # check left side
        char = map[number["start"]["y"]][number["start"]["x"]-1]
#        print(f"left char: {char}")
        if not char.isdigit() and char != ".":
#            print(f" {char} IS left ADJACENT!")
            if char == "*":
                gear_map[number["start"]["y"]][number["start"]["x"]-1] += 1
                gear_sum_map[number["start"]["y"]][number["start"]["x"]-1] *= number["value"]            
            is_adjacent = True
        x_min_limit = number["start"]["x"]-1
    
    if number["start"]["x"] + number["length"] == len(map[0]):
        x_max_limit = number["length"]+1
    else:
        # check right side
        char = map[number["start"]["y"]][number["start"]["x"]+number["length"]]
#        print(f"right char: {char}")
        if not char.isdigit() and char != ".":
#            print(f" {char} IS right ADJACENT!")
            if char == "*":
                gear_map[number["start"]["y"]][number["start"]["x"]+number["length"]] += 1
                gear_sum_map[number["start"]["y"]][number["start"]["x"]+number["length"]] *= number["value"]            
            is_adjacent = True
        x_max_limit = number["length"]+2

    if number["start"]["y"] > 0:
        # check row above
#        print(f"x_min: {x_min_limit}, x_max: {x_min_limit+x_max_limit}")
        for x in range(x_min_limit, x_min_limit+x_max_limit):
            char = map[number["start"]["y"]-1][x]
            if not char.isdigit() and char != ".":
#                print("IS ADJACENT!")
                if char == "*":
                    gear_map[number["start"]["y"]-1][x] += 1
                    gear_sum_map[number["start"]["y"]-1][x] *= number["value"]            
                is_adjacent = True
            
    if number["start"]["y"] < len(map)-1:
        # check row below
#        print(f"x_min: {x_min_limit}, x_max: {x_min_limit+x_max_limit}")
        for x in range(x_min_limit, x_min_limit+x_max_limit):
            char = map[number["start"]["y"]+1][x]
            if not char.isdigit() and char != ".":
#                print("IS ADJACENT!")
                if char == "*":
                    gear_map[number["start"]["y"]+1][x] += 1
                    gear_sum_map[number["start"]["y"]+1][x] *= number["value"]            
                is_adjacent = True
    return is_adjacent

map = []
part_numbers = []
gear_table = []
gear_sum_table = []

with open("data") as data:
    for y, line in enumerate(data):
        tmp_number = ""
        tmp_line = []
        tmp_gear_line = []
        tmp_gear_sum_line = []
        for x, char in enumerate(line.strip()):
            if len(tmp_number) <= 0:
                start_x = x
            tmp_line.append(char)
            tmp_gear_line.append(0)
            tmp_gear_sum_line.append(1)
            if char.isdigit():                    
                tmp_number+=char
            else:
                if len(tmp_number) > 0:
                    part_numbers.append({ "value": int(tmp_number), "start" : { "x" : start_x, "y" : y }, "length" : len(tmp_number) })
                tmp_number=""
            if tmp_number != "" and x == len(line.strip())-1:
                part_numbers.append({ "value": int(tmp_number), "start" : { "x" : start_x, "y" : y }, "length" : len(tmp_number) })
        map.append(tmp_line)
        gear_table.append(tmp_gear_line)
        gear_sum_table.append(tmp_gear_sum_line)

result = 0
#print(part_numbers)
#print(len(part_numbers))

for part in part_numbers:
    if check_for_adjacent(map, part, gear_table, gear_sum_table):
        result+=part["value"]

print(f"part1 : {result}")

#print(f"map {len(map[0])} x {len(map)}")
#print(f"gear_table {len(gear_table[0])} x {len(gear_table)}")
#print(f"gear_sum_table {len(gear_sum_table[0])} x {len(gear_sum_table)}")

result2 = 0
gear_count = 0

for y, row in enumerate(gear_table):
    for x, count in enumerate(row):
        if count == 2:
            result2 += gear_sum_table[y][x]
        if count > 0:
            gear_count += 1

#print(gear_count)
print(f"part2: {result2}")