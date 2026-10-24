"""Lab 2: small reproducible checks for boundaries and repeated modes."""
from lab2_model import StatefulClassroomAgent

def run_checks():
    a = StatefulClassroomAgent()
    tests = [
        ((29, True), "COOL", True),
        ((29, True), "COOL", False),
        ((26, True), "IDLE", True),
        ((20, True), "IDLE", False),
        ((19, True), "WARM", True),
        ((29, False), "ECO", True),
    ]
    for i, (percept, expected_target, expected_send) in enumerate(tests, 1):
        _, target, send = a.act(*percept)
        assert (target, send) == (expected_target, expected_send), (i, target, send)
        print(f"PASS test {i}: percept={percept}, target={target}, command={send}")
if __name__ == "__main__":
    run_checks()
