class LongChainReasoning:
    def __init__(self, mimo_client):
        self.client = mimo_client

    def plan_task(self, task_description):
        """
        Simulates Long-Chain Reasoning by creating a detailed execution plan
        before the actual generation of code or architecture.
        """
        prompt = f"Plan the execution steps for the following task in high detail:\n{task_description}"
        plan = self.client.generate(prompt)
        return plan
