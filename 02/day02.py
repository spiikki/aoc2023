# AoC 2023 / Day2
# spiikki / nalleperhe
#
# find games that would be possible with predefined bag of cubes
# sum the gameIDs as result

games = {}

target_set = { "red" : 12, "blue" : 14, "green" : 13 }
result = 0

with open("example") as data:
    for line in data:
        game = line.split(":")
        id = game[0].split()
        rounds = game[1].split(";")
        #print(f"id: {id[1]}, rounds: {len(rounds)}")
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
        print(f"after round {id}: red_max {red_max}, blue_max {blue_max}, green_max {green_max}")
        if target_set["red"] >= red_max and target_set["blue"] >= blue_max and target_set["green"] >= green_max:
            result += int(id[1])

print(result)