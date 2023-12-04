cal_values = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        num = []
        for char in line:
            try:
                number = int(char)
                num.append(number)
            except:
                continue
        if len(num) == 1:
            cal_values.append(num[0]*10+num[0])
        else:
            cal_values.append(num[0]*10+num[-1])

cal_values_sum = sum(cal_values)
print(cal_values_sum)
