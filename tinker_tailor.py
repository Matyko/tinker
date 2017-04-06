from time import time

class TinkerTailorBasic:

    def __init__(self, num, step):
        self.players = []
        self.num = num + 1
        self.step = step - 1
        self.pos = self.step

    def pick(self):
        self.players.pop(self.pos)

    def run(self):
        for i in range(1,self.num):
            self.players.append(i)
        while len(self.players) > 1:
            self.pick()
            self.pos = (self.pos + self.step) % len(self.players)
        self.print()

    def print(self):
        print("The last person is standing on number ", self.players[0], ".")

if __name__ == '__main__':
    n, s = input('Enter the number of people: '), input('Enter the number of steps: ')
    proc = TinkerTailorBasic(int(n), int(s))
    start = time()
    proc.run()
    print('Time elapsed: ', time()-start, ' seconds.')