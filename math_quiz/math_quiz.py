import random


def pickRandomInteger(min, max):
    """
    Select random integer.

    Parameters
    ----------
    min : int
        The minimum value of ramdom integer.

    max : int
        The maximum value of random integer.

    Returns
    -------
    int
        the random integer
    """

    return random.randint(min, max)


def choiceOperator():
    """
    Select random operator.

    Parameters
    ----------

    Returns
    -------
    str
        the random operator.
    """

    return random.choice(['+', '-', '*'])


def calculateFormula(num1, num2, operator):
    """
    Calculate the formular.

    Parameters
    ----------
    num1 : int
        The first number of the formula.

    num2 : int
        The second number of the formula.
    
    operator : str
        The operator of the formula.

    Returns
    -------
    int
        The anwser for the formula.
    """

    problem = f"{num1} {operator} {num2}"
    if operator == '+': anwser = num1 + num2 # if '+' is selected, do addition
    elif operator == '-': anwser = num1 - num2 # if '-' is selected, do subtraction
    else: anwser = num1 * num2 # if '*' is selected, do multiplication
    return problem, anwser

def math_quiz():

    score = 0
    TOTAL_QUESTIONS = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(TOTAL_QUESTIONS):
        # choose the numbers and an operator using the created functions
        num1 = pickRandomInteger(1, 10); num2 = pickRandomInteger(1, 5); operator = choiceOperator()

        PROBLEM, ANSWER = calculateFormula(num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")

        # check whether the user input is valid, otherwise call value error and let the user input an answer again
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer")

        # if the answer is correct, get one point
        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{TOTAL_QUESTIONS}")

if __name__ == "__main__":
    math_quiz()
