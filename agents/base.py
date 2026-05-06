from mimo_api.client import MiMoClient

class BaseAgent:
    def __init__(self, name, role, model="mimo-pro-v1"):
        self.name = name
        self.role = role
        self.client = MiMoClient(model=model)

    def execute(self, input_data):
        raise NotImplementedError("Subclasses must implement the execute method.")
