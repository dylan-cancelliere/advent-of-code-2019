INPUT_LOW = 254032
INPUT_HIGH = 789860


def main():
    count = 0
    for x in range(INPUT_LOW, INPUT_HIGH + 1):
        nums = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
        checker = True
        x = str(x)
        nums[x[0]] += 1
        for y in range(1, 6):
            nums[x[y]] += 1
            if x[y] < x[y - 1]:
                checker = False
                break
        if checker and 2 in nums.values():
            count += 1
    print(count)
    # 78876 - Too High


if __name__ == "__main__":
    main()
