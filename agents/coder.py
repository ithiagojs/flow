from .base import BaseAgent

class CoderAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Coder", role="Implementation", model="mimo-coder-v1")

    def execute(self, architecture_plan):
        print(f"[{self.name}] Generating code based on architecture...")
        code = self.client.generate(f"Write highly optimized code for: {architecture_plan}")
        return code
