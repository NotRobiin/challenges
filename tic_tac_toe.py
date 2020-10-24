def tic_tac_toe(matrix: list) -> str:
    # A list of possible layouts of Xs or Os required for a win.
    # Each element represents an index in a 1d list.
    win_layouts = [
        [0, 4, 8],
        [2, 4, 6],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]

    # 2d game board to a 1d game board.
    game = [j for i in matrix for j in i]

    # Find the solution based on the possible win layouts.
    for solution in win_layouts:
        pawns = [game[i] for i in solution]

        if len(set(pawns)) == 1:
            return pawns[0]

    return "Draw"


if __name__ == "__main__":
    print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]]))  # "X"

    print(tic_tac_toe([["O", "O", "O"], ["O", "X", "X"], ["E", "X", "X"]]))  # "O"

    print(tic_tac_toe([["X", "X", "O"], ["O", "O", "X"], ["X", "X", "O"]]))  # "Draw"
