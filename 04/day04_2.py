# AoC 2023 / Day 4
# spiikki / nalleperhe
#
# count card scores and win recursively more tickets, but how many?

result = 0
original_cards = []

with open("example") as data:
    for card in data:
        card_fields = card.split(":")
        card_id = card_fields[0]
        card_numbers = card_fields[1].split("|")
        winning_numbers = card_numbers[0].strip().split(" ")
        own_numbers = card_numbers[1].strip().split(" ")
        win_count = 0
        for win_num in winning_numbers:
            if win_num in own_numbers:
                if win_num.isdigit():
                    win_count+=1
        original_cards.append(win_count)

final_deck = []

for id in range(len(original_cards)-1, -1, -1):
    sum = 0
    value = original_cards[id]
    print(f"{id}: {value}")
    if value > 0:
        for n in range(0, value):
            sum += final_deck[n]
    sum+=1
    final_deck.insert(0, sum)

print(final_deck)

for value in final_deck:
    result += value

print(result)