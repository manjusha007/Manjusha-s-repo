import random

# Welcome message
print("Welcome to the Python learner's quick quiz!")
print("Prepare to test your Python knowledge and have some fun along the way!")

# Initialize variables
playing = True
score = 0

# Generate a set of random questions from the question bank
python_learner_questions = [
    {
        "question": "Whole numbers without decimals?",
        "answer": "integer",
    },
    {
        "question": "Numbers with decimals?",
        "answer": "float",
    },
    {
        "question": "Sequences of characters?",
        "answer": "string",
    },
    {
        "question": "Unordered and unique collections?",
        "answer": "set",
    },
    {
        "question": "Ordered and mutable collections?",
        "answer": "list",
    },
    {
        "question": "Key-value pairs?",
        "answer": "dictionary",
    },
    {
        "question": "Named storage location for data?",
        "answer": "variable",
    },
    {
        "question": "Function to display information?",
        "answer": "print",
    },
    {
        "question": "Function to get data from user?",
        "answer": "input",
    },
    {
        "question": "Equality comparison operator?",
        "answer": "==",
    },
    {
        "question": "Assignment operator?",
        "answer": "=",
    },
    {
        "question": "Data type for true or false values?",
        "answer": "boolean",
    },
    {
        "question": "Symbol for addition?",
        "answer": "+",
    },
    {
        "question": "Symbol for subtraction?",
        "answer": "-",
    },
    {
        "question": "Symbol for multiplication?",
        "answer": "*",
    },
    {
        "question": "Symbol for division?",
        "answer": "/",
    },
    {
        "question": "Symbol for modulo (remainder) operation?",
        "answer": "%",
    },
    {
        "question": "Symbol for exponent?",
        "answer": "**",
    },
]

# Shuffle the questions randomly
random.shuffle(python_learner_questions)

# Start the quiz
while playing:
    score = 0
    print("\n**Let's Play!**\n")

    # Ask each question and evaluate the user's answer
    for question in python_learner_questions:
        user_answer = input(question["question"] + ": ").lower()

        # Convert both user answer and correct answer to lowercase for case-insensitive comparison
        user_answer_lower = user_answer.strip()
        correct_answer_lower = question["answer"].strip()

        if user_answer_lower == correct_answer_lower:
            print("\n🎉 Correct! You've got the answer right! 🎉\n")
            score += 1
        else:
            print("\n🤔 Oops! That's not quite right. 🤔\n")
            print("The correct answer is:", question["answer"])

    # Display the final score and percentage
    print("\n**Your Score:**", score, "out of", len(python_learner_questions))
    percentage = (score / len(python_learner_questions)) * 100
    print("\n**Your Percentage:**", percentage, "%")

    # Check if the user wants to play again
    playing = input("\nDo you want to play another round? (yes/no): ")

    if playing.lower() != "yes":
        print("\nThanks for playing! See you next time!\n")
        break
