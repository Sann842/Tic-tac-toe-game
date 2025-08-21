class TicTacToe:

    def __init__(self):
        self.xState = [0] * 9
        self.yState = [0] * 9

    def print_game_board(self):
        def index(i):
            return 'X' if self.xState[i] else ('O' if self.yState[i] else 0)

        print(f"{index(0)} | {index(1)} | {index(2)}")
        print(f"--|---|---")
        print(f"{index(3)} | {index(4)} | {index(5)}")
        print(f"--|---|---")
        print(f"{index(6)} | {index(7)} | {index(8)}")

    def check(self):
        Wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in Wins:
            if (sum(self.xState[i] for i in win) == 3):
                self.print_game_board()
                print("A won the match.")
                return 1
            if (sum(self.yState[i] for i in win) == 3):
                self.print_game_board()
                print("B won the match.")
                return 0
        return -1

    def draw(self):
        return all(x or y for x, y in zip(self.xState, self.yState))


game = TicTacToe()
turn = 1
while (1):
    game.print_game_board()
    if turn == 1:
        print("A's turn:")
        value = int(input("Enter the index to place X: "))
        game.xState[value] = 1
        turn = 0
    else:
        print("B's turn")
        value = int(input("Enter the index to place O: "))
        game.yState[value] = 1
        turn = 1
    cwin = game.check()
    if (cwin != -1):
        break
    if game.draw():
        game.print_game_board()
        print("It's a draw!")
        break
