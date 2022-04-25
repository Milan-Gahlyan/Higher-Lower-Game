from game_data import data
from art import vs
from art import logo
import random
from replit import clear


def format_data(account):
	"""TAKES THE ACCOUNT DATA AND RETURN THE PRITABLE FORMAT"""
	account_name = account["name"]
	account_describe = account["description"]
	account_country = account["country"]
	return f"{account_name}, a {account_describe}, from {account_country}"

def check_answer(guess,a_followers, b_followers):
	"""TAKE THE USER GUESS AND FOLLOWER COUNTS AND RETURNS IF THEY GOT IT RIGHT."""
	if a_followers > b_followers:
		return guess == "a"
	else:
		return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
	clear()
	print (logo)
	
	account_a = account_b
	account_b = random.choice(data)
	while account_a == account_b:
		account_b = random.choice(data)

	print(f"Compare A: {format_data(account_a)}")
	print(vs)
	print(f"Against B: {format_data(account_b)}")

	guess = input("Who has more followers?(a/b):  ").lower() 

	a_follower_count = account_a["follower_count"]
	b_follower_count = account_b["follower_count"]

	is_correct = check_answer(guess, a_follower_count, b_follower_count)

	if is_correct:
		score += 1
		print(f"You're right!! Current score :{score}")
	else:
		game_should_continue = False
		print(f"Sorry, that's wrong!! Final score :{score}")