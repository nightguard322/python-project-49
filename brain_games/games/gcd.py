from brain_games.games.engine import launch
import random


def start() -> None:

    expressions = generate_expressions()
    config = {
        'message': "Find the greatest common divisor of given numbers.",
        'expressions': expressions
    }
    launch(config)


def generate_expressions() -> list:
    expressions = []
    numbers = generate_number_pairs()

    for num1, num2 in numbers:
        expressions.append(
            (f"{num1} {num2}", calculate(num1, num2))
        )
        
    return expressions


def calculate(num1: int, num2: int) -> int:
    if num2 == 0:
        return 0
        
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2


def generate_number_pairs() -> list:
    first_numbers_list = [random.randint(1, 100) for _ in range(3)]
    second_numbers_list = [random.randint(1, 100) for _ in range(3)]
    return zip(first_numbers_list, second_numbers_list)
    