from brain_games import utils


def launch(config: dict) -> None:
    username = utils.get_username()
    utils.show_message(f"Hello, {username}")
    utils.show_message(
        config['message']
    )
    for question, answer in config['expressions']:
        user_answer = utils.prompt_message((f"Question: {question}\n"))
        
        if user_answer.lower() == str(answer):
            utils.show_message("Correct!")
        else:
            utils.show_message(
                (
                    f"{user_answer} is wrong answer ;(. Correct answer was {answer}.\n"
                    f"Let's try again, {username}!"
                )
            )
            break
    else:
        print(f"Congratulations, {username}!")