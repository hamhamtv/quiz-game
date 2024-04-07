**quiz-game**
Python console quiz, that tests the player's general knowledge based on 15 randomly picked questions out of the pool quiz_data.py



**Description and Explanation by ChatGPT 3.5:**
This Python script is a quiz game that tests players' general knowledge. Here's a description of how it works:

1. The script imports two arrays questions and answers from a file named quiz_data.py. These arrays contain questions and their corresponding answers.
2. The script prompts the user to press 'ENTER' to start the quiz.
3. Upon starting the quiz, the quiz() function is called. Inside this function:
4. It prints a welcome message.
5. Initializes a variable score to keep track of the player's score.
6. Iterates through a loop for number_of_questions (which is set to 15) times.
7. For each iteration, it selects a random question from the questions array using random.randrange() and prints it.
8. It prompts the user for an answer and compares it with the corresponding answer from the answers array.
9. If the user's answer matches the correct answer (case-insensitive), it increments the score variable and prints a message indicating the correct answer along with the updated score.
10. If the user's answer is incorrect, it prints a message indicating the correct answer.
11. After all questions have been asked, it prints the player's final score along with a message indicating successful completion of the quiz.
12. If the user input to start the game is anything other than pressing 'ENTER', the script exits.

Overall, this quiz game provides players with a randomized set of 15 questions from the provided pool and evaluates their knowledge based on their answers.
