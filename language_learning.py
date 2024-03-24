import random
from words import *

def user(words):
    score = 0

    for word in words:
        print(f"What is {word['hungarian']} in English?")
        answer = input("Your answer: ").lower()
        correct_answer = word['english'].lower()

        if answer == correct_answer:
            print("Correct answer \n")
            score += 1
        else: print(f"Wrong answer, the correct answer is '{word['english']}' \n")

def main():
    print("This is a language learning app")
    user(words)

if __name__ == "__main__": # checks if the script is being run as a main program
    main()