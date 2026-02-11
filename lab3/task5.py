import random

class LearningAgent:
    def __init__(self):
        self.Q = {
            "Play": 0,
            "Rest": 0
        }
        self.alpha = 0.5  
    def choose_action(self):
        return random.choice(["Play", "Rest"])

    def get_reward(self, action):
        if action == "Play":
            return 5
        else:
            return 1

    def update_Q(self, action, reward):
        old_value = self.Q[action]
        new_value = old_value + self.alpha * (reward - old_value)
        self.Q[action] = new_value


agent = LearningAgent()

print("Initial Q-Table:", agent.Q)

for step in range(10):
    action = agent.choose_action()
    reward = agent.get_reward(action)
    agent.update_Q(action, reward)

    print(f"Step {step+1}: Action = {action}, Reward = {reward}")
    print("Updated Q-Table:", agent.Q)

print("Final Learned Q-Table:", agent.Q)
