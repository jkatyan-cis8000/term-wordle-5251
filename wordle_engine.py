class WordleGame:
    def __init__(self, target_word: str):
        self.target_word = target_word.upper()
        self.max_attempts = 6
        self.attempts = 0
        self.guesses = []
        self.game_over = False
        self.won = False

    def is_valid_word(self, word: str) -> bool:
        if len(word) != 5:
            return False
        if not word.isalpha():
            return False
        return True

    def guess(self, word: str) -> list[int]:
        if self.game_over:
            raise ValueError("Game is already over")
        
        word = word.upper()
        
        if not self.is_valid_word(word):
            raise ValueError("Invalid word")
        
        self.attempts += 1
        self.guesses.append(word)
        
        result = self._calculate_coloring(word)
        
        if word == self.target_word:
            self.won = True
            self.game_over = True
        elif self.attempts >= self.max_attempts:
            self.game_over = True
        
        return result

    def _calculate_coloring(self, guess: str) -> list[int]:
        result = [0] * 5
        target_freq = {}
        
        for char in self.target_word:
            target_freq[char] = target_freq.get(char, 0) + 1
        
        for i in range(5):
            if guess[i] == self.target_word[i]:
                result[i] = 2
                target_freq[guess[i]] -= 1
        
        for i in range(5):
            if result[i] == 0:
                if guess[i] in target_freq and target_freq[guess[i]] > 0:
                    result[i] = 1
                    target_freq[guess[i]] -= 1
        
        return result

    def is_game_over(self) -> bool:
        return self.game_over

    def has_won(self) -> bool:
        return self.won

    def get_attempts_left(self) -> int:
        return self.max_attempts - self.attempts
