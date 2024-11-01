#List of the question and answer
questions_and_answers = [
        ("What is the capital of France? ", "Paris"),
        ("What is the capital of Germany? ", "Berlin"),
        ("What is the capital of Italy? ", "Rome"),
        ("What is the capital of Spain? ", "Madrid"),
        ("What is the capital of Portugal? ", "Lisbon"),
        ("What is the capital of Netherlands? ", "Amsterdam"),
        ("What is the capital of Belgium? ", "Brussels"),
        ("What is the capital of Austria? ", "Vienna"),
        ("What is the capital of Sweden? ", "Stockholm"),
        ("What is the capital of Norway? ", "Oslo")
    ]
#This asks the questions
def ask_question(question, correct_answer):
    while True:
        answer = input(question).strip().lower()
        if answer == correct_answer.lower():
            print("Correct!!!!")
            break
        else:
            print("Oops, that is wrong!!!! Try again")
#What runs and make the quiz function
def main():
    print("Welcome to the European Capitals Quiz! Let's get started!")
    #Ask each question from the list
    for question, answer in questions_and_answers:
        ask_question(question, answer)

    print("Quiz complete! Thanks for playing!")
#Directly start the quiz without the conditional check
main()