# Kaun banega crorepati

import os
import sys

qna = {
    "What is the capital of India?": "Delhi",
    "What is the capital of Pakistan?": "Islamabad",
    "What is the capital of China?": "Beijing",
    "What is the capital of Nepal?": "Kathmandu",
    "What is the capital of Bangladesh?": "Dhaka",
    "What is the capital of Sri Lanka?": "Colombo",
}

ans = ["Delhi", "Islamabad", "Beijing", "Kathmandu", "Dhaka", "Colombo"]
all_answers = ""

wins = 0

print("Kaun banega crorepati. You have type name of capital city.")
print(
    "Each wins will give you 1 crore rupees and giving any wrong answer will end the game and you will get 0 rupees."
)

for i, j in enumerate(ans):
    all_answers += f"{i+1}. {j}\n"

for question, answer in qna.items():
    print("--------------------------------------------------")
    # run clear command for linux and windows using sys
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
    print(f"Current wins: {wins} crore rupees")

    user_answer = input(f"{question}\n{all_answers}")

    if user_answer.lower() == answer.lower():
        print("Correct Answer")
        wins += 1
    else:
        print("Wrong Answer")
        print("Game Over")
        print("Better luck next time")
        wins = 0
        break

if wins == 0:
    print("You won 0 rupees")
else:
    print(f"You won {wins} crore rupees")
