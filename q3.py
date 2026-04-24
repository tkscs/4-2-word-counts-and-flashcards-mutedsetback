# Update this dictionary with questions and answers:
flashcards = {
    "question": "answer"
}
import random

# Get a list of keys (questions) from the dictionary
#### YOUR CODE HERE
questions = list(flashcards.keys())
# Randomly sample one question
#### YOUR CODE HERE
question = random.choice(questions)

# Use the `input` function to ask the user the question and get their response
#### YOUR CODE HERE
response = input(question + " ")

# Use the question as a key to look up the answer in the dicitonary
#### YOUR CODE HERE
answer = flashcards[question]

# Check if the response is the same as the answer, and give the user
# feedback based on whether their response was correct or incorrect
#### YOUR CODE HERE
if response == answer:
    print("correct")