def main():
    width = 25
    height = 6
    with open("input.txt", "r") as file:
        string = file.read()
    zeros = (9999999, None)
    layer = ""
    while len(string) > width * height:
        num = 0
        layer = string[:width * height]
        string = string[width * height:]
        for i in layer:
            if i == "0":
                num += 1
        if num < zeros[0]:
            zeros = (num, layer)
    print(count("1", zeros[1]) * count("2", zeros[1]))


def decode():
    width = 25
    height = 6
    img = [[]]
    with open("input.txt", "r") as file:
        string = file.read()
    while len(string) > width * height:
        layer = string[:width * height]
        string = string[width * height:]
        counter = 0
        for i in layer:
            if counter == width:
                


def count(val, string):
    counter = 0
    for i in string:
        if i == val:
            counter += 1
    return counter


if __name__ == "__main__":
    main()
