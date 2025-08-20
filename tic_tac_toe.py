def print_game_board(xState, yState):
    zero = 'X' if xState[0] else ('O' if yState[0] else 0)
    one = 'X' if xState[1] else ('O' if yState[1] else 0)
    two = 'X' if xState[2] else ('O' if yState[2] else 0)
    three = 'X' if xState[3] else ('O' if yState[3] else 0)
    four = 'X' if xState[4] else ('O' if yState[4] else 0)
    five = 'X' if xState[5] else ('O' if yState[5] else 0)
    six = 'X' if xState[6] else ('O' if yState[6] else 0)
    seven = 'X' if xState[7] else ('O' if yState[7] else 0)
    eight = 'X' if xState[8] else ('O' if yState[8] else 0)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")


def sum(a, b, c):
    return a+b+c


def check(xState, yState):
    Wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in Wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print_game_board(xState, yState)
            print("X won the match.")
            return 1
        if (sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3):
            print_game_board(xState, yState)
            print("Y won the match.")
            return 0
    return -1


def draw(xState, yState):
    return all(x or y for x, y in zip(xState, yState))


xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1
while (True):
    print_game_board(xState, yState)
    if turn == 1:
        print("A's turn")
        value = int(input("Enter the index to place X: "))
        xState[value] = 1
        turn = 0
    else:
        print("B's turn")
        value = int(input("Enter the index to place O: "))
        yState[value] = 1
        turn = 1
    cwin = check(xState, yState)
    if (cwin != -1):
        break
    if draw(xState, yState):
        print_game_board(xState, yState)
        print("It's a draw!")
        break
