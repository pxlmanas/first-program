PRIZES = [
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000
]

questions = [
    {
        "q": "Which planet is called the Red Planet?",
        "options": {"A": "Venus", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
        "ans": "B",
    },
    {
        "q": "Who wrote the Indian National Anthem?",
        "options": {
            "A": "Bankim Chandra",
            "B": "Sarojini Naidu",
            "C": "Rabindranath Tagore",
            "D": "Subhash Chandra Bose",
        },
        "ans": "C",
    },
    {
        "q": "What is the capital of Australia?",
        "options": {
            "A": "Sydney",
            "B": "Melbourne",
            "C": "Brisbane",
            "D": "Canberra",
        },
        "ans": "D",
    },
    {
        "q": "Which gas do plants absorb from the atmosphere?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon Dioxide",
            "D": "Hydrogen",
        },
        "ans": "C",
    },
    {
        "q": "How many bones are there in the adult human body?",
        "options": {"A": "186", "B": "206", "C": "216", "D": "256"},
        "ans": "B",
    },
    {
        "q": "Which is the largest ocean on Earth?",
        "options": {
            "A": "Atlantic",
            "B": "Indian",
            "C": "Arctic",
            "D": "Pacific",
        },
        "ans": "D",
    },
    {
        "q": "What does 'CPU' stand for?",
        "options": {
            "A": "Central Processing Unit",
            "B": "Computer Personal Unit",
            "C": "Central Program Utility",
            "D": "Core Processing Unit",
        },
        "ans": "A",
    },
]

print("Welcome To Kaun Banega Crorepati")
name = input("Enter your name: ")


current_money = 0
question_number = 1

for item in questions:
    
    print("Question " + str(question_number) + " for Rs. " + str(PRIZES[question_number - 1]))
    print(item["q"])
    print("A) " + item["options"]["A"])
    print("B) " + item["options"]["B"])
    print("C) " + item["options"]["C"])
    print("D) " + item["options"]["D"])

    while True:
        choice = input("Your answer (A, B, C, or D): ").upper().strip()

        if choice in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input! Try again.")

    if choice == item["ans"]:
        current_money = PRIZES[question_number - 1]
        print("Correct! You won Rs. " + str(current_money))
        question_number = question_number + 1
    else:
        print("Wrong Answer! The correct answer was " + item["ans"])
        print("Game Over. You take home Rs. " + str(current_money))
        break
else:
    print("CONGRATULATIONS " + name + "!! YOU WON THE GRAND PRIZE: Rs. " + str(current_money))