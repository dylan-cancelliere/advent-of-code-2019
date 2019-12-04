def main():
    intersections = []
    path = []

    with open("input.txt", "r") as file:
        wire1 = file.readline().strip().split(",")
        wire2 = file.readline().strip().split(",")
        x = 0
        y = 0

        for instruction in wire1:
            num = int(instruction[1:])
            if instruction[0] == "R":
                for i in range(1, num + 1):
                    path.append((x + i, y))
                x += num
            elif instruction[0] == "L":
                for i in range(1, num + 1):
                    path.append((x - i, y))
                x -= num
            elif instruction[0] == "U":
                for i in range(1, num + 1):
                    path.append((x, y + i))
                y += num
            elif instruction[0] == "D":
                for i in range(1, num + 1):
                    path.append((x, y - i))
                y -= num

        x = 0
        y = 0
        for instruction in wire2:
            num = int(instruction[1:])
            if instruction[0] == "R":
                for i in range(1, num + 1):
                    if (x + i, y) in path:
                        intersections.append((x + i, y))
                x += num
            elif instruction[0] == "L":
                for i in range(1, num + 1):
                    if (x - i, y) in path:
                        intersections.append((x - i, y))
                x -= num
            elif instruction[0] == "U":
                for i in range(1, num + 1):
                    if (x, y + i) in path:
                        intersections.append((x, y + i))
                y += num
            elif instruction[0] == "D":
                for i in range(1, num + 1):
                    if (x, y - i) in path:
                        intersections.append((x, y - i))
                y -= num
        print(intersections)


intersections = (-1084, 917), (-592, 923), (-488, 917), (-488, 866), (645, -6), (709, 0), (709, 226), (709, 750), (565, 963), (565, 1391), (565, 1712), (617, 2344), (827, 2344), (827, 1712), (493, 1515), (161, 1262), (-210, 866), (444, -678), (742, -495), (749, -495), (1089, -484), (1089, -428), (1089, -99), (1089, -15), (919, 410), (726, 410), (645, 410), (379, 410), (375, 558), (1307, 750), (919, 690), (887, 750), (887, 841), (717, 1051), (454, 963), (178, 963), (717, 1024), (938, 750), (1557, 129), (1549, 750), (1399, 750), (1208, 1712), (1297, 2030), (717, 1151), (537, 963), (537, 558), (537, 529), (645, 368), (726, 368), (919, 368), (919, 514), (912, 750), (912, 841), (1567, -651), (1567, -587), (1511, -415), (953, -428), (953, -484), (953, -651), (953, -794), (749, -957), (500, -979), (500, -1041), (500, -1461), (500, -1492), (651, -1692), (674, -1692), (860, -1692), (1124, -1692), (1200, -1692), (1795, -1577), (1930, -1577), (1999, -1577), (2009, -1577), (2284, -1467), (2359, -1467), (2373, -1467), (2439, -1529), (2439, -1596), (2440, -1606), (2496, -1606), (2777, -1606), (3338, -2076), (3220, -2949), (2795, -3233), (2910, -3654), (2876, -3654), (3199, -3233), (3252, -2967), (3400, -2967), (3758, -2705), (3820, -2457), (3874, -2705), (3874, -2797), (3400, -3197), (3318, -2949), (3665, -2346), (3517, -2076), (2777, -1653), (2440, -1653), (2236, -1653), (2461, -2456), (2236, -2433), (1732, -3665), (1343, -3801), (1109, -3801), (780, -3801), (758, -3393), (758, -3159), (850, -3068), (970, -3068), (970, -3391), (949, -3332), (850, -3173), (559, -3159), (559, -3051), (559, -2893), (561, -2893), (561, -3051), (561, -3159), (349, -3234), (349, -3301), (447, -3393), (447, -3681), (447, -3906), (447, -4144), (447, -4208), (426, -4278), (237, -4278), (110, -4278), (-362, -4487), (-362, -4666), (-362, -5140), (-773, -5187), (-3025, -1821), (-2396, -1821), (-2254, -2185), (-1696, -2738), (-1226, -2738), (-1124, -2738), (-1037, -2738), (-1012, -2991), (-1012, -3020), (-1037, -3127), (-1124, -3127), (-1226, -3127), (-1645, -3127), (-1696, -3127), (-1812, -3127), (-1588, -2634), (-1588, -2991), (-1588, -3020), (-1645, -3639), (-2463, -3042)


def manhattan_intersection():
    small = 999999999
    for item in intersections:
        tot = abs(item[0]) + abs(item[1])
        if tot < small:
            small = tot
    print(small)


def signal_loss():
    with open("input.txt", "r") as file:
        wire1 = file.readline().strip().split(",")
        wire2 = file.readline().strip().split(",")
    test(wire1)
    test(wire2)

    small = 999999999
    for item in intersections:
        w1steps = calc_steps(wire1, item)
        w2steps = calc_steps(wire2, item)
        if w1steps + w2steps < small:
            small = w1steps + w2steps
            print(small)


def calc_steps(wire, intersect):
    x = 0
    y = 0
    steps = 0
    for instruction in wire:
        num = int(instruction[1:])
        if instruction[0] == "R":
            for i in range(1, num + 1):
                if (x + i, y) == intersect:
                    return steps + i
            x += num
            steps += num
        elif instruction[0] == "L":
            for i in range(1, num + 1):
                if (x - i, y) == intersect:
                    return steps + i
            x -= num
            steps += num
        elif instruction[0] == "U":
            for i in range(1, num + 1):
                if (x, y + i) == intersect:
                    return steps + i
            y += num
            steps += num
        elif instruction[0] == "D":
            for i in range(1, num + 1):
                if (x, y - i) == intersect:
                    return steps + i
            y -= num
            steps += num


def test(wire):
    total = 0
    for instruction in wire:
        total += int(instruction[1:])
    print(total, "Test")


if __name__ == "__main__":
    signal_loss()
