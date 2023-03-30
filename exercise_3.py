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

all_questions = [_ for _ in qna.keys()]

all_ans = [_ for _ in qna.values()]


all_answers = ""

wins = 0

print("Kaun banega crorepati. You have type name of capital city.")
print(
    "Each wins will give you 1 crore rupees and giving any wrong answer will end the game and you will get 0 rupees."
)

for i in range(len(all_questions)):
    print("Current wins: {} crore rupees.".format(wins))
    print(all_questions[i])
    all_answers = input("Enter your answer: ")
    if all_answers == all_ans[i]:
        wins += 1
        print("You are right. You won {} crore rupees.".format(wins))
    else:
        print("You are wrong. You won 0 crore rupees.")
        sys.exit()
