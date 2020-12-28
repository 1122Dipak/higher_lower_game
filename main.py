from art import logo, vs
from game_data import data
import random

print(logo)
game_end = True
while game_end:
    A = random.randint(0, 50)
    score = 0
    print(f"Compare A: {data[A]['name']}, {data[A]['description']}, {data[A]['country']}")
    print(vs)
    B = random.choice([i for i in range(0, 50) if i not in [A]])
    print(f"Against B: {data[B]['name']}, {data[B]['description']}, {data[B]['country']}")
    choice = input("Who has more followers? Choose 'A' or 'B' : ")
    if choice.lower() == "a":
        if data[A]['follower_count'] > data[B]['follower_count']:
            score += 1
            print(f"You are right! Current score {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_end = True
            break
    else:
        if data[A]['follower_count'] < data[B]['follower_count']:
            score += 1
            print(f"You are right! Current score {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_end = True
            break
