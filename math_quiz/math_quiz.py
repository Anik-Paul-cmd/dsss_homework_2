import random


def generate_random_integer(min_value, max_value):
    
    """
    Generate a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    
    """
    Generate a random arithmetic operator: '+', '-', or '*'.
    """

    return random.choice(['+', '-', '*'])


def calculate_result(num_1, num_2, operator):

    """
    Calculate the result of the arithmetic operation defined by num_1, num_2, and operator.
    """

    question = f"{num_1} {operator} {num_2}"
    
    if operator == '+': 
        result = num_1 + num_2
        
    elif operator == '-': 
        result = num_1 - num_2
        
    else: 
        result = num_1 * num_2
        
    return question, result


def get_user_answer():
    """
    Get and validate user input as an integer.
    """
    while True:
        
        try:
            user_input = input("Your answer: ")
            user_answer = int(user_input)
            return user_answer
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
            
            

def math_quiz():
    
    """
    Run the Math Quiz Game.
    """
    
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num_1 = generate_random_integer(1, 10)
        num_2 = generate_random_integer(1, 10) 
        operator = generate_random_operator()

        problem, answer = calculate_result(num_1, num_2, operator)
        print(f"\nQuestion: {problem}")
        
        user_answer = get_user_answer()
        
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
