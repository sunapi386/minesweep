
import random

class Cell(object):
    def __init__(self, is_mine, is_visible=False, is_flagged=False):
        self.is_mine = is_mine
        self.is_visible = is_visible
        self.is_flagged = is_flagged

    def __str__(self):
        if cell.is_visible:
            if cell.is_mine:
                return "M"
            else:
                return "?"
        elif cell.is_flagged:
            return "F"
        else:
            return "X"

    def fromchar(char):
        self.is_mine = False
        self.is_visible = False
        self.is_flagged = False
        if char == 'M':
            self.is_mine = True
            self.is_visible = True
        elif char == '?':
            self.is_visible = True
        elif char == 'F':
            self.is_flagged = True


    def show(self):
        self.is_visible = True

    def flag(self):
        self.is_flagged = not self.is_flagged

    def place_mine(self):
        self.is_mine = True


class Board(tuple):
    def __init__(self, tup):
        self.is_playing = True

    def mine_repr(self,row_id, col_id):
        cell = self[row_id][col_id]
        if cell.is_visible:
            if cell.is_mine:
                return "M"
            else:
                surr = self.count_surrounding(row_id, col_id)
                return str(surr) if surr else " "
        elif cell.is_flagged:
            return "F"
        else:
            return "X"

    def __str__(self):
        board_string = ""
        for (row_id, row) in enumerate(self):
            board_string += ("".join(self.mine_repr(row_id, col_id) \
                for (col_id, _) in enumerate(row)))
        return board_string

    def to_list(self):
        lst = []
        for (row_id, row) in enumerate(self):
            lst.append(
                [self.mine_repr(row_id, col_id) for (col_id, col) in enumerate(row)]
            )
        return lst

    def show(self, row_id, col_id):
        cell = self[row_id][col_id]
        if not cell.is_visible:
            cell.show()

            if (cell.is_mine and not
                cell.is_flagged):
                self.is_playing = False
            elif self.count_surrounding(row_id, col_id) == 0:
                for (surr_row, surr_col) in self.get_neighbours(row_id, col_id):
                    if self.is_in_range(surr_row, surr_col):
                        self.show(surr_row, surr_col)

    def flag(self, row_id, col_id):
        cell = self[row_id][col_id]
        if not cell.is_visible:
            cell.flag()
        else:
            print("Cannot add flag, cell already visible.")

    def place_mine(self, row_id, col_id):
        self[row_id][col_id].place_mine()

    def count_surrounding(self, row_id, col_id):
        return sum(1 for (surr_row, surr_col) in self.get_neighbours(row_id, col_id)
                        if (self.is_in_range(surr_row, surr_col) and
                            self[surr_row][surr_col].is_mine))

    def get_neighbours(self, row_id, col_id):
        SURROUNDING = ((-1, -1), (-1,  0), (-1,  1),
                       (0 , -1),           (0 ,  1),
                       (1 , -1), (1 ,  0), (1 ,  1))
        return ((row_id + surr_row, col_id + surr_col) for (surr_row, surr_col) in SURROUNDING)

    def is_in_range(self, row_id, col_id):
        return 0 <= row_id < len(self) and 0 <= col_id < len(self)

    @property
    def remaining_mines(self):
        remaining = 0
        for row in self:
            for cell in row:
                if cell.is_mine:
                    remaining += 1
                if cell.is_flagged:
                    remaining -= 1
        return remaining

    @property
    def is_solved(self):
        # every cell is either revealed or a mine
        return all((cell.is_visible or cell.is_mine) for row in self for cell in row)

def create_board(size, mines):
    board = Board(tuple([tuple([Cell(False) for i in range(size)])
                         for j in range(size)]))
    available_pos = list(range((size-1) * (size-1)))
    for i in range(mines):
        new_pos = random.choice(available_pos)
        available_pos.remove(new_pos)
        (row_id, col_id) = (new_pos % 9, new_pos // 9)
        board.place_mine(row_id, col_id)
    return board

def load_board(board_lst):
    if type(board_lst) == list:
        board = Board(tuple([tuple(b) for b in board_lst]))
        return board
    print "load_board: bad board representation type", str(type(board_lst))

def get_move(board):
    INSTRUCTIONS = ("First, enter the column, followed by the row. To add or "
                    "remove a flag, add \"f\" after the row (for example, 64f "
                    "would place a flag on the 6th column, 4th row). Enter "
                    "your move: ")

    move = input("Enter your move (for help enter \"H\"): ")
    if move == "H":
        move = input(INSTRUCTIONS)

    while not is_valid(move, board):
        move = input("Invalid input. Enter your move (for help enter \"H\"): ")
        if move == "H":
            move = input(INSTRUCTIONS)

    return (int(move[1]), int(move[0]), move[-1] == "f")

def make_move(board, move):
    """ Move representation: column + row + <f>. To add or "
        "remove a flag, add \"f\" after the row (for example, 64f "
        "would place a flag on the 6th column, 4th row). """
    if 2 <= len(move) and len(move) <= 3:
        (row_id, col_id, is_flag) = (int(move[1]), int(move[0]), move[-1] == "f")
        if is_flag:
            board.flag(row_id, col_id)
        else:
            board.show(row_id, col_id)

def is_valid(move_input, board):
    if move_input == "H" or (len(move_input) not in (2, 3) or
                             not move_input[:1].isdigit() or
                             int(move_input[0]) not in range(len(board)) or
                             int(move_input[1]) not in range(len(board))):
        return False

    if len(move_input) == 3 and move_input[2] != "f":
        return False

    return True

def result(board):
    if board.is_playing and not board.is_solved:
        return "continue"
    elif board.is_solved:
        return "win"
    else:
        return "lost"

def main():
    SIZE = 10
    MINES = 9
    board = create_board(SIZE, MINES)
    print(board)

    # while board.is_playing and not board.is_solved:
    #     (row_id, col_id, is_flag) = get_move(board)
    #     if not is_flag:
    #         board.show(row_id, col_id)
    #     else:
    #         board.flag(row_id, col_id)
    #     print(board)

    # if board.is_solved:
    #     print("Well done! You solved the board!")
    # else:
    #     print("Uh oh! You blew up!")

if __name__ == "__main__":
    main()
