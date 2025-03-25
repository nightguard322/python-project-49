from brain_games import utils
from brain_games.games.engine import launch
import random

def start() -> None:
    expressions = generate_expressions()
    config = {
        'message': "What number is missing in the progression?.",
        'expressions': expressions
    }
    launch(config)


def generate_expressions() -> list:
    progressions = []
    for _ in range(3):
        progression = generate_progression()
        answer = random.choice(progression)
        answer_index = progression.index(answer)
        progression[answer_index] = '..'
        progressions.append(
            (progression, answer)
        )
    return progressions


def generate_progression() -> list:
    diff = random.randint(2, 5)
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    return [start + (num - 1) * diff for num in range(1, length)]