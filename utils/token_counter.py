class TokenCounter:
    def __init__(self):
        self.total_tokens = 0

    def count(self, text):
        """
        Simulates token counting for processing millions of tokens efficiently.
        Approximates 1 token per 4 characters.
        """
        tokens = len(str(text)) // 4
        self.total_tokens += tokens
        return tokens
