from agents.architect import ArchitectAgent
from agents.coder import CoderAgent
from agents.critic import CriticAgent
from utils.token_counter import TokenCounter
from core.memory import ContextCompressionLayer

class Orchestrator:
    def __init__(self):
        self.architect = ArchitectAgent()
        self.coder = CoderAgent()
        self.critic = CriticAgent()
        self.token_counter = TokenCounter()
        self.context_layer = ContextCompressionLayer()

    def run_flow(self, task_description):
        print("Starting MIMO-Flow Orchestration...\n")
        self.token_counter.count(task_description)
        self.context_layer.add_event("User", "Task_Request", task_description)
        
        # Step 1: Architect (System Design & Reasoning)
        architecture = self.architect.execute(task_description)
        self.token_counter.count(architecture)
        self.context_layer.add_event(self.architect.name, "Generated_Plan", architecture)
        
        # Trigger Context Compression before heavy coding
        self.context_layer.compress_context()
        
        # Step 2: Coder (Implementation)
        code = self.coder.execute(architecture)
        self.token_counter.count(code)
        self.context_layer.add_event(self.coder.name, "Generated_Code", code)
        
        # Step 3: Critic (Review & Refinement)
        # Pass compressed context + code to Critic
        self.context_layer.compress_context()
        feedback = self.critic.execute(code)
        self.token_counter.count(feedback)
        self.context_layer.add_event(self.critic.name, "Code_Review", feedback)
        
        print("\n" + "="*40)
        print("MIMO-FLOW FINAL OUTPUT")
        print("="*40)
        print(f"Architecture: {architecture}\n")
        print(f"Code: {code}\n")
        print(f"Feedback: {feedback}\n")
        print("-" * 40)
        print(f"Total Tokens Processed: {self.token_counter.total_tokens}")
        print("\n[Telemetry] Generating session log...")
        
        return code, feedback
