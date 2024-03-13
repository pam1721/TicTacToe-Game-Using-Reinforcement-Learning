import random

class RLAgent:
    def __init__(self, symbol, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.symbol = symbol
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_values = {}  # Dictionary to store Q-values

    def choose_action(self, available_moves, board_state):
        # Convert board_state list to tuple to make it hashable
        state_key = tuple(board_state)
        if random.random() < self.exploration_rate:
            return random.choice(available_moves)  # Explore: choose a random action
        else:
            # Exploit: choose the action with the highest Q-value
            max_q_value = float('-inf')
            best_action = None
            for action in available_moves:
                q_value = self.q_values.get((state_key, action), 0)  # Get Q-value or default to 0
                if q_value > max_q_value:
                    max_q_value = q_value
                    best_action = action
            return best_action

    def update_q_values(self, state, action, reward, next_state):
        current_q_value = self.q_values.get((state, action), 0)
        max_next_q_value = max([self.q_values.get((next_state, next_action), 0) for next_action in range(9)], default=0)
        new_q_value = current_q_value + self.learning_rate * (reward + self.discount_factor * max_next_q_value - current_q_value)
        self.q_values[(state, action)] = new_q_value
