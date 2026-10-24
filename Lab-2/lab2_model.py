"""Lab 2: stateful agent avoids sending the same target command twice."""
class StatefulClassroomAgent:
    def __init__(self, initial_mode=None):
        self.previous_mode = initial_mode

    @staticmethod
    def target_mode(temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"

    def act(self, temp, occupied):
        previous = self.previous_mode
        target = self.target_mode(temp, occupied)
        send_command = target != previous
        self.previous_mode = target
        return previous, target, send_command

if __name__ == "__main__":
    agent = StatefulClassroomAgent()
    percepts = [(29, True), (29, True), (26, True), (20, True), (19, True), (29, False)]
    print("step | previous | percept | target | command")
    for i, p in enumerate(percepts, 1):
        prev, target, send = agent.act(*p)
        print(i, prev, p, target, "SEND" if send else "NO COMMAND")
