import numpy as np


class BlackJack:
    def __init__(self, s_0=None):
        self.CARD_VALUE = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                           '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
        self.player_cards = []
        self.dealer_cards = []
        if (s_0 is None):
            self.player_ace = 0
            self.player_total = 0

            self.dealer_ace = 0
            self.dealer_total = 0

            while self.player_total < 12:
                self.player_draw()
            for i in range(2):
                self.dealer_draw()
        else:
            self.player_total, self.player_ace, self.dealer_total = s_0
            self.dealer_ace = 0
            if self.dealer_total == 1:
                self.dealer_ace += 1
                self.dealer_total = 11
            self.dealer_draw()

        self.finish = False

    def show_status(self):
        print("-"*20)
        print("Player (total : {0}) [ {1} ]".format(
            self.player_total, ", ".join(self.player_cards)))

        if self.finish:
            print("Dealer (total : {0}) [ {1} ]".format(
                self.dealer_total, ", ".join(self.dealer_cards)))
        else:
            print("Dealer (total : ??) [ {1}, ?? ]".format(
                self.dealer_total, ", ".join(self.dealer_cards), (self.dealer_total if self.dealer_total != 11 else 1)))
        print("-"*20)

    def state(self):
        if self.finish:
            res = self.result()
            if res > 0:
                return "PlayerWin"
            elif res < 0:
                return "PlayerLose"
            else:
                return "Draw"
        else:
            return (self.player_total, int(self.player_ace > 0), self.CARD_VALUE[self.dealer_cards[0]])

    def player_hit(self):
        self.player_draw()
        if self.player_total > 21:
            self.finish = True

    def player_stand(self):
        while self.dealer_total < 17:
            self.dealer_draw()
        self.finish = True

    def player_draw(self):
        draw_card = np.random.choice(
            ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
        self.player_cards.append(draw_card)
        self.player_total += self.CARD_VALUE[draw_card]
        if draw_card == 'A':
            self.player_ace += 1
        if self.player_total > 21 and self.player_ace > 0:
            self.player_total -= 10
            self.player_ace -= 1

    def dealer_draw(self):
        draw_card = np.random.choice(
            ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
        self.dealer_cards.append(draw_card)
        self.dealer_total += self.CARD_VALUE[draw_card]
        if draw_card == 'A':
            self.dealer_ace += 1
        if self.dealer_total > 21 and self.dealer_ace > 0:
            self.dealer_total -= 10
            self.dealer_ace -= 1

    def result(self):
        reward = 0
        if self.player_total > 21:
            reward = -1
        elif self.dealer_total > 21:
            reward = 1
        elif self.player_total > self.dealer_total:
            reward = 1
        elif self.player_total < self.dealer_total:
            reward = -1
        else:
            reward = 0
        return reward


if __name__ == "__main__":
    game = BlackJack()
    print()
    while True:
        game.show_status()
        s = input("[h] : hit, [s] : stand, [q] : quit\n")
        if s == "h":
            game.player_hit()
        elif s == "s":
            game.player_stand()
        elif s == "q":
            break
        else:
            print("Wrong Input")
            continue

        if game.finish:
            break

    game.show_status()
    result = game.result()
    if result > 0:
        print("Player Win!")
    elif result < 0:
        print("Player Lose!")
    else:
        print("Draw.")
