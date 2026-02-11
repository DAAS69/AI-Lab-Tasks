class FireEnvironment:
    def __init__(self):
        self.rooms = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }

    def display(self):
        print("\nCurrent Building Status:")
        symbols = []
        for room in self.rooms.values():
            if room == 'fire':
                symbols.append('F')#fire
            else:
                symbols.append('.')   #safe

        for i in range(0, 9, 3):
            print(" ".join(symbols[i:i+3]))

    def extinguish_fire(self, room):
        self.rooms[room] = 'safe'


class FireRobot:
    def __init__(self):
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

    def start_mission(self, env):
        for room in self.path:
            print(f"\nRobot enters room {room}")

            if env.rooms[room] == 'fire':
                print("Fire detected! Extinguishing...")
                env.extinguish_fire(room)
            else:
                print("Room is safe.")

            env.display()


environment = FireEnvironment()
robot = FireRobot()

robot.start_mission(environment)

print("Mission Complete: All fires extinguished!")
environment.display()
