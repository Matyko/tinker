from datetime import datetime


class TinkerTailorBasic:

    def __init__(self, num, step):
        self.players = []
        self.result = []
        self.num = num + 1
        self.step = step - 1
        self.pos = self.step

    def pick(self):
        picked = self.players.pop(self.pos)
        self.result.append(picked)

    def setup(self):
        for i in range(1,self.num):
            self.players.append(i)

    def loop(self):
        while len(self.players) > 0:
            self.pick()
            if self.players:
                self.pos = (self.pos + self.step) % len(self.players)

    def print(self):
        print("The players were picked in the following order: ", self.result)

    def run(self):
        self.setup()
        self.loop()
        self.print()

if __name__ == '__main__':
    n, s = input('Enter the number of people: '), input('Enter the number of steps: ')
    proc = TinkerTailorBasic(int(n), int(s))
    start = datetime.now()
    proc.run()
    print('Time elapsed: ', datetime.now()-start, '.')