with open("inputs/day4.txt") as file:
    data = [line.strip() for line in file]

input_nrs = [int(x) for x in data[:1][0].split(',')]
boards = []
board = []
for row in data[2:]:
    if not row:
        boards.append(board)
        board = []
    else:
        board.append([int(x) for x in row.split()])

boards.append(board)

def check_bingo(board):
    for idx, row in enumerate(board):
        # check row and column
        if all(x == 'x' for x in row) or all(x == 'x' for x in [row[idx] for row in board]):
            return True

    return False


def mark_board_nr(boards, board, board_idx):
    for row_idx, row in enumerate(board):
        boards[board_idx][row_idx] = ['x' if x == nr else x for x in row]
        if check_bingo(board):
            return True

    return False


# Part 1
part1 = 0
for nr in input_nrs:
    for board_idx, board in enumerate(boards):
        if mark_board_nr(boards, board, board_idx):
            part1 = sum(
                [item for sublist in board for item in sublist if item != 'x']) * nr
            break
    if part1 > 0:
        break

# Part 2
completed_boards = []
part2 = 0
for nr in input_nrs:
    for board_idx, board in enumerate(boards):
        board_done = mark_board_nr(boards, board, board_idx)
        if board_done and not board_idx in completed_boards:
            completed_boards.append(board_idx)

        if len(boards) == len(completed_boards):
            part2 = sum(
                [item for sublist in board for item in sublist if item != 'x']) * nr
            break

    if part2 > 0:
        break

print("Part 1", part1)
print("Part 2", part2)
