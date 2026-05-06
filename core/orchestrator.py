from agents.architect import ArchitectAgent
from agents.coder import CoderAgent
from agents.critic import CriticAgent
from utils.token_counter import TokenCounter

class Orchestrator:
    def __init__(self):
        self.architect = ArchitectAgent()
        self.coder = CoderAgent()
        self.critic = CriticAgent()
        self.token_counter = TokenCounter()

    def run_flow(self, task_description):
        print("Starting MIMO-Flow Orchestration...\n")
        self.token_counter.count(task_description)
        
        # Step 1: Architect (System Design & Reasoning)
        architecture = self.architect.execute(task_description)
        self.token_counter.count(architecture)
        
        # Step 2: Coder (Implementation)
        code = self.coder.execute(architecture)
        self.token_counter.count(code)
        
        # Step 3: Critic (Review & Refinement)
        feedback = self.critic.execute(code)
        self.token_counter.count(feedback)
        
        print("\n" + "="*40)
        print("MIMO-FLOW FINAL OUTPUT")
        print("="*40)
        print(f"Architecture: {architecture}\n")
        print(f"Code: {code}\n")
        print(f"Feedback: {feedback}\n")
        print("-" * 40)
        print(f"Total Tokens Processed: {self.token_counter.total_tokens}")
        
        return code, feedback
