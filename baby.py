# Baby Conversation Simulator using loopy loops

from random import choice

questions = ["Why is the sky blue?: ", "Why is there a face on the moon?: ",
             "Is there such thing as Santa Claus?: ", "Why are there dinosaurs?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("Oh... okay.")
