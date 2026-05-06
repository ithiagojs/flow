from .base import BaseAgent
from core.reasoning import LongChainReasoning

class ArchitectAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Architect", role="System Design", model="mimo-architect-v1")
        self.reasoning = LongChainReasoning(self.client)

    def execute(self, task_description):
        print(f"[{self.name}] Planning architecture for task using Long-Chain Reasoning...")
        plan = self.reasoning.plan_task(task_description)
        architecture = f"Architecture based on plan: {plan}"
        return architecture
