import day5.day5


def main():
    num_amps = 5
    phase_setting = [0, 1, 2, 3, 4]
    input_signal = 0
    larg = -1
    for a in range(num_amps):
        phase_setting[0] = a
        for b in range(num_amps):
            phase_setting[1] = b
            for c in range(num_amps):
                phase_setting[2] = c
                for d in range(num_amps):
                    phase_setting[3] = d
                    for e in range(num_amps):
                        phase_setting[4] = e
                        for i in range(num_amps):
                            input_signal = day5.day5.main("/home/dylan/cs/adventofcode/day7/input.txt", phase_setting[i], input_signal)
                            if input_signal == "Break":
                                break
                        if input_signal != "Break" and input_signal > larg:
                            if len(phase_setting) == len(set(phase_setting)):
                                larg = input_signal
                        input_signal = 0
    print(larg)


def part2():
    phase_setting = [0, 1, 2, 3, 4]
    input_signal = 0
    larg = -1
    for a in range(5, 10):
        phase_setting[0] = a
        for b in range(5, 10):
            phase_setting[1] = b
            for c in range(5, 10):
                phase_setting[2] = c
                for d in range(5, 10):
                    phase_setting[3] = d
                    for e in range(5, 10):
                        phase_setting[4] = e
                        phase_setting = [9, 8, 7, 6, 5]
                        while True:
                            for i in range(5):
                                input_signal = day5.day5.main("/home/dylan/cs/adventofcode/day7/test_input.txt", phase_setting[i], input_signal)
                                if input_signal == "Break":
                                    break
                            if input_signal != "Break" and input_signal > larg:
                                if len(phase_setting) == len(set(phase_setting)):
                                    larg = input_signal
                            elif input_signal == "Break":
                                break
                        input_signal = 0
    print(larg)


if __name__ == "__main__":
    part2()
