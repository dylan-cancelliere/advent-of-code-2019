def main():
    tot = 0
    with open("1/input.txt") as file:
        for line in file:
            ans = line
            while True:
                ans = int(int(ans) / 3) - 2
                if ans < 1:
                    break
                tot += ans
    print(tot)


if __name__ == "__main__":
    main()
