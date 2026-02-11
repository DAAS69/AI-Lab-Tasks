class StudyAgent:
    def __init__(self):
        self.subjects = ["AI", "Math", "Physics"]

    def act(self):
        if self.subjects:
            subject = self.subjects.pop(0)
            print(f"Studying {subject}")
        else:
            print("Goal Achieved: All subjects completed")


agent = StudyAgent()

while agent.subjects:
    agent.act()

agent.act()
