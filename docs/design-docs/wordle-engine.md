# Wordle Engine Design Document

## Implementation Summary

Created `wordle_engine.py` with `WordleGame` class implementing:

### Core Methods

1. **`__init__(target_word: str)`**: Initializes game with target word, sets max attempts to 6

2. **`is_valid_word(word: str) -> bool`**: Validates words are 5 letters and alphabetic only

3. **`guess(word: str) -> list[int]`**: Processes guess, returns 5-element color list:
   - 0 = grey (letter not in word or excess occurrences)
   - 1 = yellow (correct letter, wrong position)
   - 2 = green (correct letter, correct position)

4. **`is_game_over() -> bool`**: Returns true if game ended (win or 6 attempts used)

5. **`has_won() -> bool`**: Returns true if last guess matched target

6. **`get_attempts_left() -> int`**: Returns remaining attempts (0-6)

### Coloring Algorithm

The `_calculate_coloring` method handles duplicate letters correctly:

1. **First pass**: Mark all greens (exact matches), decrementing frequency count
2. **Second pass**: Mark yellows only if letter exists in remaining frequency

### Example: Target="ABBEY", Guess="BUBBLE"

- B at position 0: target has B's at 0,1, but position 0 is U → check frequency
- U at position 1: not in target → grey (0)
- B at position 2: target B at 0,1 available → yellow (1)
- B at position 3: target B at 0,1 available → yellow (1)
- L at position 4: not in target → grey (0)

## Files Created

- `wordle_engine.py` - Main game engine implementation

## No Issues Encountered

Implementation completed successfully.
