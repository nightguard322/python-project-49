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
    diff = random.randint(1, 5)
    length = random.randint(5, 10)
    progression = [num + diff for num in range(length)]
    answer = random.choice(progression)
    progression.remove(answer)
    return progression