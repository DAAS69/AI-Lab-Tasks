class TrafficEnvironment:
    def __init__(self, traffic_state):
        self.traffic_state = traffic_state 
        
    def get_percept(self):
        return self.traffic_state


class TrafficReflexAgent:
    def act(self, percept):
        if percept == "Heavy":
            return "Extend Green Time"
        else:
            return "Normal Green"


def run_agent(agent, environment):
    percept = environment.get_percept()
    action = agent.act(percept)
    print(f"Percept: {percept} Traffic → Action: {action}")


env1 = TrafficEnvironment("Heavy")
env2 = TrafficEnvironment("Light")
agent = TrafficReflexAgent()

run_agent(agent, env1)
run_agent(agent, env2)
