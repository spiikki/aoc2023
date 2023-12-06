# AoC 2023 / Day 4
# spiikki / nalleperhe
#
# count card scores and sum all scores as result

result = 0
with open("data") as data:
    for card in data:
        card_fields = card.split(":")
        card_id = card_fields[0]
        print(card_id)
        card_numbers = card_fields[1].split("|")
        winning_numbers = card_numbers[0].strip().split(" ")
        own_numbers = card_numbers[1].strip().split(" ")
        win_count = 0
        card_value = 0
        print(winning_numbers)
        print(own_numbers)
        for win_num in winning_numbers:
            if win_num in own_numbers:
                if win_num.isdigit():
                    win_count+=1
                    print(f"win! {win_num}")
        if win_count > 0:
            card_value = 1
            for i in range(1, win_count):
                card_value += card_value
        result += card_value
print(result)