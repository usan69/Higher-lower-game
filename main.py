from art import logo, vs
from data import data
import random
from replit import clear


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f" {account_name} , a {account_desc}, from {account_country}"


def check_answer(guess, a_follwers_count, b_follwers_count):
    if a_follwers_count > b_follwers_count:
        return guess == "a"
    else:
        return guess == "b"


score = 0
print(logo)
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"CompareA: {format_data(account_a)}.")
    print(vs)
    print(f"CompareB: {format_data(account_b)}.")

    guess = input("Who has more follwerss ? 'A' or 'B' : ").lower()

    a_follwers_count = account_a["follower_count"]
    b_follwers_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follwers_count, b_follwers_count)
    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"It's correect. Current score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry!  You are  wrong. Final score :{score}")

