DIGITS = {"one": 1, "two": 2, "three": 3, "four": 4,
          "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
TENS = {"ten": 10, "twenty": 20, "thirty": 30, "forty": 40,
        "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
HUNDRED = 100
THOUSAND = 1000
MILLION = 1000000


def find_all_indices(main_string, substring):
    indices = []
    index = main_string.find(substring)

    while index != -1:
        indices.append([index, DIGITS[substring] % 10])
        index = main_string.find(substring, index + 1)

    return indices


cal_values = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        indices_num = []
        for x in range(len(line)):
            char = line[x]
            try:
                number = int(char)
                indices_num.append([x, number])
            except:
                continue
        for digits in DIGITS.keys():
            indices = find_all_indices(line, digits)
            for index in indices:
                indices_num.append(index)
        for tens in TENS.keys():
            indices = find_all_indices(line, tens)
            for index in indices:
                indices_num.append(index)
        indices_num.sort()
        indices_num = [x[1] for x in indices_num]
        if len(indices_num) == 1:
            cal_values.append(indices_num[0]*10+indices_num[0])
        else:
            cal_values.append(indices_num[0]*10+indices_num[-1])

print(sum(cal_values))
