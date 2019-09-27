import numpy as np


class MaruBatu:
    def __init__(self):
        self.end = False
        self.winner = None
        self.state = np.zeros((3, 3))

    def play(self, line, row):
        self.state[line, row] = 1

        if self.eval() == 1:
            self.end = True
            self.winner = "PLAYER"
            return

        line, row = self.__cpuPlay()

        if self.eval() == 2:
            self.end = True
            self.winner = "ENEMY"
            return

    def showState(self):
        for i in range(3):
            for j in range(3):
                if self.state[i, j] == 1:
                    print("o", end=" ")
                elif self.state[i, j] == 2:
                    print("x", end=" ")
                else:
                    print("-", end=" ")
            print()

    def eval(self):
        if ((self.state[line, :] == 1).all() or (self.state[:, row] == 1).all() or
                (self.state[0, 0] == self.state[1, 1] == self.state[2, 2] == 1) or (self.state[0, 2] == self.state[1, 1] == self.state[2, 0] == 1)):
            return 1

        if ((self.state[line, :] == 2).all() or (self.state[:, row] == 2).all() or
                (self.state[0, 0] == self.state[1, 1] == self.state[2, 2] == 2) or (self.state[0, 2] == self.state[1, 1] == self.state[2, 0] == 2)):
            return 2

        return 0

    def __cpuPlay(self):
        idx = np.random.choice(
            [(3*line+row) for line in range(3) for row in range(3) if self.state[line, row] == 0])
        line, row = idx//3, idx % 3
        self.state[line, row] = 2
        return line, row


if __name__ == "__main__":
    game = MaruBatu()
    while not game.end:
        game.showState()
        line, row = map(int, input().split(" "))
        game.play(line, row)

    print(game.winner)
