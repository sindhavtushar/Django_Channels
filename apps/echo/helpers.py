import random

def generate_board():
    board = []

    # Columns B, I, N, G, O
    columns = [
        range(1, 16),     # B
        range(16, 31),    # I
        range(31, 46),    # N
        range(46, 61),    # G
        range(61, 76)     # O
    ]

    for col_idx, col_range in enumerate(columns):
        # Pick 5 random numbers from the column range
        numbers = random.sample(col_range, 5)
        board.append(numbers)

    # Transpose columns → rows
    board_rows = [list(row) for row in zip(*board)]

    # Optional: make center cell free
    board_rows[2][2] = "FREE"

    return board_rows