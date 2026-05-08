#!/usr/bin/env python3
"""
Term Wordle - A terminal-based Wordle game
"""

import random
import os
import sys

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from words import WORD_LIST, get_daily_word, is_valid_word
from wordle_engine import WordleGame


# ANSI color codes
GREEN = "\033[92m\033[1m"
YELLOW = "\033[93m\033[1m"
GREY = "\033[90m"
RESET = "\033[0m"


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def color_letter(letter: str, status: int) -> str:
    """Return a letter colored based on its status."""
    if status == 2:  # Green - correct position
        return f"{GREEN}{letter}{RESET}"
    elif status == 1:  # Yellow - wrong position
        return f"{YELLOW}{letter}{RESET}"
    else:  # Grey - invalid
        return f"{GREY}{letter}{RESET}"


def display_board(guesses: list[str], results: list[list[int]], attempts: int, attempts_left: int):
    """Display the game board with colored letters."""
    clear_screen()
    print("=" * 50)
    print("       TERM WODLE")
    print("=" * 50)
    print()
    
    # Display guesses with colors
    for i, guess in enumerate(guesses):
        result = results[i]
        colored_guess = "".join(color_letter(guess[i], result[i]) for i in range(5))
        print(f"  {i + 1}. {colored_guess}")
    
    # Display empty rows
    for _ in range(6 - len(guesses)):
        print("  . _ _ _ _ _")
    
    print()
    print(f"  Attempts left: {attempts_left}")
    print()


def display_message(message: str, msg_type: str = "info"):
    """Display a message to the user."""
    print()
    if msg_type == "win":
        print(f"{GREEN}  {message}{RESET}")
    elif msg_type == "lose":
        print(f"{YELLOW}  {message}{RESET}")
    elif msg_type == "error":
        print(f"{GREY}  {message}{RESET}")
    else:
        print(f"  {message}")
    print()


def get_user_guess(attempt_num: int) -> str:
    """Get a valid guess from the user."""
    while True:
        try:
            guess = input(f"  Enter your guess (attempt {attempt_num}/6): ").strip().upper()
            
            if guess == "QUIT" or guess == "EXIT":
                return "QUIT"
            
            if not guess:
                display_message("Please enter a 5-letter word.", "info")
                continue
            
            if len(guess) != 5:
                display_message("Invalid: Word must be exactly 5 letters.", "error")
                continue
            
            if not guess.isalpha():
                display_message("Invalid: Word must contain only letters.", "error")
                continue
            
            if not is_valid_word(guess):
                display_message("Invalid: Word not in dictionary.", "error")
                continue
            
            return guess
            
        except KeyboardInterrupt:
            return "QUIT"
        except EOFError:
            return "QUIT"


def play_wordle():
    """Main game loop."""
    # Initialize game
    target_word = get_daily_word().upper()
    game = WordleGame(target_word)
    
    guesses = []
    results = []
    
    clear_screen()
    print("=" * 50)
    print("       TERM WODLE")
    print("=" * 50)
    print()
    print("  Rules:")
    print("  - Guess the 5-letter word in 6 attempts")
    print("  - Green = correct letter, correct position")
    print("  - Yellow = correct letter, wrong position")
    print("  - Grey = letter not in word")
    print()
    print("  Type 'quit' to exit")
    print()
    
    while not game.is_game_over():
        attempts_left = game.get_attempts_left()
        display_board(guesses, results, len(guesses), attempts_left)
        
        guess = get_user_guess(game.attempts + 1)
        
        if guess == "QUIT":
            print()
            print(f"  Thanks for playing! The word was: {target_word}")
            print()
            return
        
        # Process guess
        result = game.guess(guess)
        guesses.append(guess)
        results.append(result)
    
    # Game over - show final state
    display_board(guesses, results, len(guesses), 0)
    
    if game.has_won():
        display_message(f"  Congratulations! You guessed '{target_word}' in {len(guesses)} attempts!", "win")
    else:
        display_message(f"  Better luck next time! The word was: {target_word}", "lose")
    
    print()


if __name__ == "__main__":
    try:
        play_wordle()
    except KeyboardInterrupt:
        print()
        print("  Thanks for playing!")
        print()
