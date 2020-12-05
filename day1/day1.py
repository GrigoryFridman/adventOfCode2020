with open("/home/grigory/AdventOfCode/2020/day1/input.txt", "r") as file:
    nums = file.readlines()
    for sm in nums:
        m = int(sm)
        for sn in nums:
            n = int(sn)
            for so in nums:
                o = int(so)
                if m + n + o == 2020:
                    print(m * n * o)
                    exit(0)
