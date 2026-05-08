def _color_letter(letter: str, status: int) -> str:
    """Color a single letter based on its status."""
    if status == 2:
        # Green: correct position
        return f"\033[92m\033[1m{letter}\033[0m"
    elif status == 1:
        # Yellow: correct letter, wrong position
        return f"\033[93m\033[1m{letter}\033[0m"
    else:
        # Grey: not in word
        return f"\033[90m{letter}\033[0m"


def display_board(guesses: list[str], results: list[list[int]], attempts: int) -> None:
    """Display the game board with colored letters and remaining attempts."""
    print("\n" + "=" * 23)
    print("       WORDLE")
    print("=" * 23 + "\n")
    
    for guess, result in zip(guesses, results):
        colored_guess = "".join(_color_letter(letter, status) for letter, status in zip(guess, result))
        print(colored_guess)
    
    for _ in range(6 - len(guesses)):
        print("\033[90m_ _ _ _ _\033[0m")
    
    print(f"\nAttempts remaining: {attempts}")


def display_message(message: str, message_type: str) -> None:
    """Display a message with appropriate styling based on type."""
    reset = "\033[0m"
    
    if message_type == "win":
        print(f"\n\033[92m\033[1m{message}\033[0m")
    elif message_type == "loss":
        print(f"\n\033[91m\033[1m{message}\033[0m")
    elif message_type == "error":
        print(f"\n\033[91m{message}\033[0m")
    elif message_type == "info":
        print(f"\n\033[93m{message}\033[0m")
    else:
        print(f"\n{message}")


def get_user_guess(attempt_num: int) -> str:
    """Prompt the user for a guess and validate input."""
    while True:
        guess = input(f"\nAttempt {attempt_num + 1}: Enter your 5-letter guess: ").strip().upper()
        
        if not guess.isalpha():
            display_message("Error: Please enter only letters.", "error")
            continue
        
        if len(guess) != 5:
            display_message("Error: Please enter exactly 5 letters.", "error")
            continue
        
        return guess
