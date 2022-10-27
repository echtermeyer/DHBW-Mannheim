import string
import random


luck_strings = list(string.ascii_uppercase)
random.shuffle(luck_strings)
print(''.join(luck_strings))

names = """"""


def sort_by_best_match(name_list, string_seq):

    still_in = {x.upper() for x in name_list}
    already_out = []

    for letter in string_seq:
        remove = {x for x in still_in if letter not in x}
        if remove:
            already_out.extend(list(remove))
        if remove == still_in:
            print(f"The winner is: {random.choice(list(still_in))}")
            break
        still_in = still_in - remove
        if len(still_in) == 1:
            print(f"The winner is: {still_in.pop()}")
            break

        # print(f"{len(still_in)} candidates left: {', '.join(list(still_in))}")


if __name__ == "__main__":
    sort_by_best_match(names.split('\n'), luck_strings)
