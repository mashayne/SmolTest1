class Counter:
    def __init__(self):
        self.count = 0

    def start_counting(self):
        while self.count < 10:
            self.count += 1
            return self.count
