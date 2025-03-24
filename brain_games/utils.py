import prompt

def prompt_message(message):
    return prompt.string(message)

def show_message(message):
    print (message)

def greet():
    show_message('Welcome to the Brain Games!')

def get_username():
    username = prompt_message("May I have your name? ")
    return username