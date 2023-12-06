# AoC 2023 / Day2
# spiikki / nalleperhe
#
# find the minimum set of cubes for round
# calculate the sum of power of rounds (multiply minimums for power)

result = 0

with open("data") as data:
    for line in data:
        game = line.split(":")
        id = game[0].split()
        rounds = game[1].split(";")
        red_max = 0
        blue_max = 0
        green_max = 0
        for round in rounds:
            colors = round.split(",")
            for color in colors:
                tmp = color.split()
                dice_amount = int(tmp[0])
                dice_type = tmp[1]
                if dice_type == "red":
                    if dice_amount > red_max:
                        red_max = dice_amount
                if dice_type == "blue":
                    if dice_amount > blue_max:
                        blue_max = dice_amount
                if dice_type == "green":
                    if dice_amount > green_max:
                        green_max = dice_amount
        power = red_max * green_max * blue_max
        print(f"round {id}: power {power}")
        result += power

print(result)