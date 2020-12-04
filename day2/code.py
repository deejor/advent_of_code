import re

def main(list):
    total = 0
    for x in list:
        numbers = re.findall(r'\d+', x)
        splittext = x.split()
        char = splittext[1]
        char = char[:1]
        if check(int(numbers[0]), int(numbers[1]), char, splittext[2]) is True:
            print(int(numbers[0]), int(numbers[1]), char, splittext[2])
            total = total + 1
        else:
            pass
    return total


def check(min, max, char, password):
    number_of_occurences = password.count(char)
    if number_of_occurences >= min and number_of_occurences <= max:
        print(number_of_occurences)
        return True
    else:
        return False
