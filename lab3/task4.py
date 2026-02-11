class UtilityAgent:
    def __init__(self):
        self.restaurants = {"A": {"distance": 3, "rating": 7}, "B": {"distance": 5, "rating": 9} }

    def calculate_utility(self, r):
        return r["rating"] - r["distance"]

    def choose_restaurant(self):
        best_choice = None
        best_utility = -999

        for name, data in self.restaurants.items():
            utility = self.calculate_utility(data)
            print(f"Restaurant {name} Utility = {utility}")

            if utility > best_utility:
                best_utility = utility
                best_choice = name

        print(f"Selected Restaurant: {best_choice}")


agent = UtilityAgent()
agent.choose_restaurant()
