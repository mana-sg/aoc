power_sum = 0
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        game_number = int(line.split(":")[0].split(" ")[1])
        line = line.split(":")[1][1:len(line.split(":")[1])-1]
        games = line.split("; ")
        green_min = 0
        red_min = 0
        blue_min = 0
        for game in games:
            print(game)
            subgame = game.split(", ")
            for ball in subgame:
                num, color = ball.split(" ")
                if color == "red" and int(num) > red_min:
                    red_min = int(num)
                elif color == "green" and int(num) > green_min:
                    green_min = int(num)
                elif color == "blue" and int(num) > blue_min:
                    blue_min = int(num)
        power = red_min*blue_min*green_min
        power_sum += power
        print(red_min, green_min, blue_min)
print(power_sum)
