from brain_games import utils
import random

def start() -> None:
    username = utils.get_username()
    utils.show_message(
        f"Hello, {username}\n Answer \"yes\" if the number is even, otherwise answer \"no\"."
    )

    for game in range(3):
        question = random.randint(1, 100)
        user_answer = utils.prompt_message(f"Question: {question}\n")
        answer = get_answer(question % 2 == 0)

        if user_answer.lower() == answer:
            utils.show_message("Correct!")
        else:
            utils.show_message(
                f"{user_answer} is wrong answer ;(. Correct answer was {answer}.\n Let's try again, {username}!"
            )
            break
    else:
        print(f"Congratulations, {username}!")


def get_answer(result: bool) -> str:
    return 'yes' if result else 'no'