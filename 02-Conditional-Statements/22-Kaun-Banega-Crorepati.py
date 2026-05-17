print("===== Welcome to KAUN BANEGA CROREPATI (KBC)! =====")

start = input("Do you want to start the game? (yes/no): ")

if start.lower() == "yes":

    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B",
            "points": 1000
        },

        {
            "question": "2. Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C",
            "points": 2000
        },

        {
            "question": "3. Who is known as the Father of Computer?",
            "options": ["A. Charles Babbage", "B. Newton", "C. Einstein", "D. Tesla"],
            "answer": "A",
            "points": 3000
        },

        {
            "question": "4. Which language is used for Python programming?",
            "options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
            "answer": "B",
            "points": 5000
        },

        {
            "question": "5. How many continents are there in the world?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "C",
            "points": 10000
        }
    ]

    score = 0
    correct = 0
    skipped = 0
    wrong = 0

    for q in questions:

        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        print("Type SKIP to skip the question")

        user_answer = input("Enter your answer (A/B/C/D): ")

        if user_answer.upper() == "SKIP":
            print("Question skipped!")
            skipped += 1

        elif user_answer.upper() == q["answer"]:
            print("Correct Answer!")
            score += q["points"]
            correct += 1

        else:
            print("Wrong Answer!")
            wrong += 1

    print("\n===== Game Over =====")
    print("Total Score:", score)
    print("Correct Answers:", correct)
    print("Skipped Questions:", skipped)
    print("Wrong Answers:", wrong)

else:
    print("Game exited. Thank you!")