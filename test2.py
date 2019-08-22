game_name = "Mario"
AGE = 34
PLAYER = 3
player_score = {}

for i in range(0, PLAYER, 1):
    user_name = input("Enter user name: ")
    score = input("Enter Score: ")
    player_score[user_name] = score
print("Name: {} \nAge: {}".format(game_name, AGE))

for key in player_score:
    print("{} _ {}".format(key, player_score[key]))
