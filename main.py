# Importing data from the quiz_data.py arrays
from quiz_data import questions, answers
import random

number_of_questions = 15


def quiz():
    print("\n\n\n\nWelcome to the quiz. \nThis quiz will focus on general knowledge. You will be asked 15 questions!")
    score = 0
    for i in range(number_of_questions):
        question_number = random.randrange(0,39)
        print("\n\nQuestion Number", i + 1, ":", questions[question_number])
        answer = input()
        if answer.lower() == answers[question_number].lower():
            score += 1
            print(" --> Correct Answer! // Your score is", score, "//", answers[question_number])
        else:
            print(" --> Wrong Answer!  // Your score is", score, "// The correct answer would've been:", answers[question_number])

    print("\n\n\n\nYou successfully completed 15 questions with a score of:", score, "\n")



start_game = input("To start playing the quiz press 'ENTER': ")
if start_game == '':
    quiz()
else:
    quit()