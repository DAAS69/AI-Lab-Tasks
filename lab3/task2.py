import random

class ClassroomEnvironment:
    def __init__(self):
        self.light_status = random.choice(["ON", "OFF"])

    def get_percept(self):
        students_present = random.choice(["Yes", "No"])
        return {"students": students_present, "light": self.light_status}

    def turn_on_light(self):
        self.light_status = "ON"

    def turn_off_light(self):
        self.light_status = "OFF"


class ModelBasedLightAgent:
    def __init__(self):
        self.model = {"previous_students": None, "previous_light": None}

    def update_model(self, percept):
        self.model["previous_students"] = percept["students"]
        self.model["previous_light"] = percept["light"]

    def act(self, percept):
        self.update_model(percept)

        if percept["students"] == "Yes" and percept["light"] == "OFF":
            return "Turn ON Lights"
        elif percept["students"] == "No" and percept["light"] == "ON":
            return "Turn OFF Lights"
        else:
            return "No Action"


def run_agent(agent, env, steps=8):
    for step in range(steps):
        percept = env.get_percept()
        action = agent.act(percept)

        if action == "Turn ON Lights":
            env.turn_on_light()
        elif action == "Turn OFF Lights":
            env.turn_off_light()

        print(f"Step {step+1}: Percept={percept}, Action={action}, Model={agent.model}")


env = ClassroomEnvironment()
agent = ModelBasedLightAgent()
run_agent(agent, env)
