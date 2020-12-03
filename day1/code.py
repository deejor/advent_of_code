def part_1(list):
    for x in list:
        for y in list:
            if(x + y) == 2020:
                return x + y


def part_2(list):
    for x in list:
        for y in list:
            for z in list:
                if(x + y + z) == 2020:
                    return x + y + z
