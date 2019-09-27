import numpy as np


class Nim:
    """ Nimゲーム """

    def __init__(self):
        self.end = False
        self.winner = None
        self.stone = np.random.randint(3, 10, size=3)

    def play(self, idx, num):
        self.stone[idx] -= num

        if all([(i == 0) for i in self.stone]):
            self.end = True
            self.winner = "CPU"
            return

        self.__cpuPlay()

        if all([(i == 0) for i in self.stone]):
            self.end = True
            self.winner = "Player"
            return

    def __cpuPlay(self):
        idx = np.random.choice([i for i in range(3) if self.stone[i] > 0])
        num = np.random.randint(1, self.stone[idx]+1)
        self.stone[idx] -= num


if __name__ == "__main__":
    nim = Nim()
    while not nim.end:
        print(nim.stone)
        idx, num = map(int, input().split(" "))
        nim.play(idx, num)

    print(nim.winner)
