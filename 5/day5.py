def main():
    with open("/home/dylan/cs/adventofcode/5/input.txt", "r") as file:
        file = file.read().split(",")
        file = [int(i) for i in file]
    i = 0
    while True:
        if len(str(file[i])) == 1:
            if file[i] == 1 or file[i] == 2:
                addition = True
                if file[i] == 2:
                    addition = False
                op12(file, i, (0, 0, 0), addition)
                i += 4
            elif file[i] == 3:
                file[file[i + 1]] = 5  # int(input("Enter number: "))
                i += 2
            elif file[i] == 4:
                print(file[file[i + 1]])
                i += 2
            elif file[i] == 5:
                i += op5(file, i, (0, 0))
            elif file[i] == 6:
                i += op6(file, i, (0, 0))
            elif file[i] == 7:
                op7(file, i, (0, 0, 0))
                i += 4
            elif file[i] == 8:
                op8(file, i, (0, 0, 0))
                i += 4
        else:
            opcode = int(str(file[i])[-2:])
            pm = []
            addition = True
            if opcode == 99:
                return "Break"
            elif opcode == 4:
                cmd = int(str(file[i])[:-2])
                if cmd == 0:
                    print(file[file[i + 1]])
                else:
                    print(file[i + 1])
                i += 2
            elif opcode == 5:
                cmd = str(file[i])[:-2]
                pm = get_pm(cmd)
                i += op5(file, i, pm)
            elif opcode == 6:
                cmd = str(file[i])[:-2]
                pm = get_pm(cmd)
                i += op6(file, i, pm)
            elif opcode == 7:
                cmd = str(file[i])[:-2]
                pm = get_pm(cmd)
                op7(file, i, pm)
                i += 4
            elif opcode == 8:
                cmd = str(file[i])[:-2]
                pm = get_pm(cmd)
                op8(file, i, pm)
                i += 4
            else:
                cmd = str(file[i])[:-2]
                pm = get_pm(cmd)
                if opcode == 2:
                    addition = False
                op12(file, i, pm, addition)
                i += 4


def get_pm(cmd):
    pm = []
    if len(cmd) == 0:
        pm = (0, 0, 0)
    elif len(cmd) == 1:
        pm = (int(cmd), 0, 0)
    else:
        pm = (int(cmd[1]), int(cmd[0]), 0)
    return pm


def op12(file, idx, pm, addition):
    num1 = 0
    num2 = 0
    if pm[0] == 0:
        num1 = file[file[idx + 1]]
    else:
        num1 = file[idx + 1]
    if pm[1] == 0:
        num2 = file[file[idx + 2]]
    else:
        num2 = file[idx + 2]
    if addition:
        file[file[idx + 3]] = num1 + num2
    else:
        file[file[idx + 3]] = num1 * num2
    return file


def op5(file, idx, pm):
    if pm[0] == 0:
        if file[file[idx + 1]] != 0:
            if pm[1] == 0:
                return file[file[idx + 2]] - idx
            else:
                return file[idx + 2] - idx
        else:
            return 3
    else:
        if file[idx + 1] != 0:
            if pm[1] == 0:
                return file[file[idx + 2]] - idx
            else:
                return file[idx + 2] - idx
        else:
            return 3


def op6(file, idx, pm):
    if pm[0] == 0:
        if file[file[idx + 1]] == 0:
            if pm[1] == 0:
                return file[file[idx + 2]] - idx
            else:
                return file[idx + 2] - idx
        else:
            return 3
    else:
        if file[idx + 1] == 0:
            if pm[1] == 0:
                return file[file[idx + 2]] - idx
            else:
                return file[idx + 2] - idx
        else:
            return 3


def op7(file, idx, pm):
    if pm[0] == 0:
        if pm[1] == 0:
            if file[file[idx + 1]] < file[file[idx + 2]]:
                file[file[idx + 3]] = 1
            else:
                file[file[idx + 3]] = 0
        else:
            if file[file[idx + 1]] < file[idx + 2]:
                file[file[idx + 3]] = 1
            else:
                file[file[idx + 3]] = 0
    else:
        if pm[1] == 0:
            if file[idx + 1] < file[file[idx + 2]]:
                file[file[idx + 3]] = 1
            else:
                file[file[idx + 3]] = 0
        else:
            if file[idx + 1] < file[idx + 2]:
                file[file[idx + 3]] = 1
            else:
                file[file[idx + 3]] = 0


def op8(file, idx, pm):
    if pm[0] == 0:
        if pm[1] == 0:
            if file[file[idx + 1]] == file[file[idx + 2]]:
                file[file[idx + 3]] = 1
            else:
                file[file[idx + 3]] = 0
        else:
            if file[file[idx + 1]] == file[idx + 2]:
                file[file[idx + 3]] = 1
            else:
                file[file[idx + 3]] = 0
    else:
        if pm[1] == 0:
            if file[idx + 1] == file[file[idx + 2]]:
                file[file[idx + 3]] = 1
            else:
                file[file[idx + 3]] = 0
        else:
            if file[idx + 1] == file[idx + 2]:
                file[file[idx + 3]] = 1
            else:
                file[file[idx + 3]] = 0


def tester():
    with open("/home/dylan/cs/adventofcode/5/input.txt", "r") as file:
        file = file.read().split(",")
        file = [int(i) for i in file]
    while True:
        print(file[int(input("Enter index value: "))])


if __name__ == "__main__":
    main()
