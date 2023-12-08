count_wrong = 0
total_count = 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        game_number = int(line.split(":")[0].split(" ")[1])
        line = line.split(":")[1][1:len(line.split(":")[1])-1]
        games = line.split("; ")
        for game in games:
            print(game)
            control = 0
            subgame = game.split(", ")
            for ball in subgame:
                num, color = ball.split(" ")
                if color == "red" and int(num) > 12:
                    count_wrong += (game_number)
                    control = 1
                    break
                elif color == "blue" and int(num) > 14:
                    count_wrong += (game_number)
                    control = 1
                    break
                elif color == "green" and int(num) > 13:
                    count_wrong += (game_number)
                    control = 1
                    break
            if (control):
                control = 0
                break
        total_count += game_number

print(total_count - count_wrong)
