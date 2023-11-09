#!/usr/bin/env Python3

def main():
    print("Welcome to the Hogwarts House Sorting Quiz!")
    print("Answer the following questions to find out which house you belong to.")
    print("Please answer with 'A', 'B', 'C', or 'D' for each question.")

    questions = [
        "Q1. What is your preferred way of spending a free afternoon?",
        "A. Reading a book",
        "B. Exploring a mysterious forest",
        "C. Socializing with friends",
        "D. Experimenting with magical objects",
        "",
        "Q2. What animal do you find most fascinating?",
        "A. Owl",
        "B. Unicorn",
        "C. Lion",
        "D. Snake",
        "",
        "Q3. What quality do you value the most?",
        "A. Intelligence",
        "B. Courage",
        "C. Loyalty",
        "D. Ambition",
    ]

    answers = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
    }

    for i in range(0, len(questions), 5):
        print(questions[i])
        for j in range(i + 1, i + 5):
            print(questions[j])
        user_answer = input("Your answer: ").strip().upper()
        if user_answer in answers:
            answers[user_answer] += 1
        else:
            print("Invalid answer. Please choose 'A', 'B', 'C', or 'D'.")

    house = max(answers, key=answers.get)
    print(f"Congratulations! You've been sorted into House {get_house_name(house)}.")

def get_house_name(letter):
    houses = {"A": "Gryffindor", "B": "Hufflepuff", "C": "Ravenclaw", "D": "Slytherin"}
    return houses.get(letter)

if __name__ == "__main__":
    main()