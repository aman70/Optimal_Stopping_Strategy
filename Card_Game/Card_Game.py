import numpy as np

class card_game:

    def card_game(red,black):
        values = [0,1]
        payoff_matrix = np.zeros((red + 1, black + 1))
        weights = []
        for i in range(1,black+1):
            payoff_matrix[0,i] = i

        for i in range(1,red+1):
            for j in range(1,black+1):
                probability_black = j/(i + j)
                probability_red = 1 - probability_black
                weights.append(probability_red)
                weights.append(probability_black)
                choice = np.random.choice(np.arange(0,2), p=[float(probability_red),float(probability_black)])
                payoff_matrix[i,j] = max(0,probability_red*(-1 + payoff_matrix[i-1,j]) \
                                     + probability_black*(1 + payoff_matrix[i,j-1]))

                weights = []


        return payoff_matrix


if __name__ == "__main__":
    print(card_game.card_game(5,5))



