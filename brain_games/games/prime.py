from brain_games import utils
from brain_games.games.engine import launch
import random

def start() -> None:

    expressions = generate_expressions()
    config = {
        'message': "Answer \"yes\" if the number is even, otherwise answer \"no\".",
        'expressions': expressions
    }
    launch(config)


def get_answer(result: bool) -> str:
    return 'yes' if result else 'no'


def generate_expressions() -> list:
    questions = random.sample(range(2, 100), 3)
    answers = [get_answer(calculate(question)) for question in questions]
    return zip(questions, answers)

def calculate(num: int) -> bool:
    if num < 2:
        return false
    for div in range(2, int(num ** 0.5) + 1): #79
        if num % div == 0:
            return False
    return True