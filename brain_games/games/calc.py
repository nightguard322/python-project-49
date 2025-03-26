from brain_games.games.engine import launch
import random

def start() -> None:

    expressions = generate_expressions()
    config = {
        'message': "What is the result of the expression?",
        'expressions': expressions
    }
    launch(config)


def get_answer(result: bool) -> str:
    return 'yes' if result else 'no'

def get_action() -> str:
    # actions = ['+', '-', '*', '/']
    actions = ['+', '-']
    return random.choice(actions)

def generate_expressions() -> list:
    expressions = []
    
    fisrt_numbers_list = [random.randint(1, 100) for _ in range(3)]
    secound_numbers_list = [random.randint(1, 100) for _ in range(3)]

    for num1, num2 in zip(fisrt_numbers_list, secound_numbers_list):
        action = get_action()

        while action == '/' and num2 == 0:
            action = get_action()

        expressions.append(
            (f"{num1} {action} {num2}", calculate(num1, num2, action))
        )
        
    return expressions

def calculate(num1: int, num2: int, action: str) -> int:

    match(action):
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if (num2 == 0):
                raise ValueError('division by zero')
            return num1 // num2
        case _:
            raise ValueError(f'Unsupported action {action}')