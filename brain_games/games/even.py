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
    questions = random.sample(range(1, 100), 3)
    answers = [get_answer(question % 2 == 0) for question in questions]
    return zip(questions, answers)