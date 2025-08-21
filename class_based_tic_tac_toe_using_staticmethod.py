class TicTacToe:

    xState = [0] * 9
    yState = [0] * 9

    @staticmethod
    def print_game_board(xState, yState):
        def index(i):
            return 'X' if xState[i] else ('O' if yState[i] else 0)

        print(f"{index(0)} | {index(1)} | {index(2)}")
        print(f"--|---|---")
        print(f"{index(3)} | {index(4)} | {index(5)}")
        print(f"--|---|---")
        print(f"{index(6)} | {index(7)} | {index(8)}")

    @staticmethod
    def check(xState, yState):
        Wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in Wins:
            if (sum(xState[i] for i in win) == 3):
                TicTacToe.print_game_board(xState, yState)
                print("A won the match.")
                return 1
            if (sum(yState[i] for i in win) == 3):
                TicTacToe.print_game_board(xState, yState)
                print("B won the match.")
                return 0
        return -1

    @staticmethod
    def draw(xState, yState):
        return all(x or y for x, y in zip(xState, yState))


game = TicTacToe
turn = 1
while (1):
    game.print_game_board(game.xState, game.yState)
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
    cwin = game.check(game.xState, game.yState)
    if (cwin != -1):
        break
    if game.draw(game.xState, game.yState):
        game.print_game_board(game.xState, game.yState)
        print("It's a draw!")
        break
