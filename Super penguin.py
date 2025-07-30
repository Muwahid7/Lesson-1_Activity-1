class bird:
    def __init__(self):
        print("Bird is ready")
    def who_is_this(self):
        print("bird")
    def swim(self):
        print("swim faster")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("The penguin is ready")
    def run(self):
        print("Run faster")
Paul = penguin()
Paul.who_is_this()
Paul.run()
Paul.swim()