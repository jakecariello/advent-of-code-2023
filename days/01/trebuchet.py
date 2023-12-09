with open("input.txt", "r") as f:
    lines = f.readlines()
    result = 0
    for line in lines:
        digits = list(filter(lambda x: int(x.isdigit()), line))
        result += int(digits[0] + digits[-1])
    print(result)
