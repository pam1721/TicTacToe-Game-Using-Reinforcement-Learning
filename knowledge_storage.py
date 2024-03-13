class KnowledgeStorage:
    def __init__(self):
        self.knowledge = {}  # Dictionary to store learned information

    def store(self, state, action, value):
        if state not in self.knowledge:
            self.knowledge[state] = {}
        self.knowledge[state][action] = value

    def retrieve(self, state, action):
        if state in self.knowledge and action in self.knowledge[state]:
            return self.knowledge[state][action]
        return None
