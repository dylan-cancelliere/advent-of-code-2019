def main(input):
    if input is None:
        with open("2/input.txt", "r") as file:
            file = file.read().split(",")
            file = [int(i) for i in file]
    else:
        file = input
    for x in range(0, len(file), 4):
        if file[x] == 1:
            file[file[x+3]] = file[file[x+1]] + file[file[x+2]]
        elif file[x] == 2:
            file[file[x+3]] = file[file[x+1]] * file[file[x+2]]
        elif file[x] == 99:
            break
        else:
            print("Bad input:", file[x])
    return file[0]


def main2():
    for x in range(0, 100):
        for y in range(0, 100):
            with open("2/input.txt", "r") as file:
                file = file.read().split(",")
                file = [int(i) for i in file]
                file[1] = x
                file[2] = y
                if main(file) == 19690720:
                    print(str(100 * x + y))


if __name__ == "__main__":
    main2()
