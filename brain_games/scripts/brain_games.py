from brain_games import utils


def main():
    utils.greet()
    username = utils.get_username()
    utils.show_message(f"Hello, {username}")

if __name__ == "__main__":
    main()