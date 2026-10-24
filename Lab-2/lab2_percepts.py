"""Lab 2: reflex classroom agent. Run: python lab2_percepts.py."""
class ClassroomAgent:
    def act(self, temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"

if __name__ == "__main__":
    agent = ClassroomAgent()
    percepts = [(29, True), (24, True), (29, False), (20, True), (26, True), (19, True)]
    for step, percept in enumerate(percepts, 1):
        print(step, percept, "target mode", agent.act(*percept))
