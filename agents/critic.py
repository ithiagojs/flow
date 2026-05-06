from .base import BaseAgent

class CriticAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Critic", role="Review and Refine", model="mimo-critic-v1")

    def execute(self, code):
        print(f"[{self.name}] Reviewing code and suggesting improvements...")
        feedback = self.client.generate(f"Review the following code and suggest optimizations for millions of tokens: {code}")
        return feedback
