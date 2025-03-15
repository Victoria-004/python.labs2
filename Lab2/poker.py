def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key

def longest_sequence(cards):
    insertion_sort(cards)
    jokers = cards.count(0)
    cards_no_jokers = [card for card in cards if card != 0]
    cards_no_jokers = list(set(cards_no_jokers))

    if not cards_no_jokers:
        return jokers

    max_len = 0
    for card in cards_no_jokers:
        current_len = 1
        current_seq = [card]
        remaining_jokers = jokers
        next_expected = card + 1

        while True:
            if next_expected in cards_no_jokers:
                current_len += 1
                current_seq.append(next_expected)
                next_expected += 1
            elif remaining_jokers > 0:
                current_len += 1
                current_seq.append(next_expected)
                next_expected += 1
                remaining_jokers -= 1
            else:
                break

        max_len = max(max_len, current_len)

    return max_len

cards = [0, 10, 15, 50, 0, 14, 9, 12, 40]
print(longest_sequence(cards))

cards2 = [1, 1, 1, 2, 1, 1, 3]
print(longest_sequence(cards2))

cards3 = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 0, 0]
print(longest_sequence(cards3))

cards4 = [2, 5, 0, 3, 4, 1, 3]
print(longest_sequence(cards4))