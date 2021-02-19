import copy

class Sudoku(object):
    def __init__(self, board):
        self.board = board
        self.solved_board = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def set_board(self,board) -> None:
        self.board = board

    def __str__(self) -> str:
        display = '+----------------+----------------+----------------+----------------+\n'
        for row_count, row in enumerate(self.solved_board, start=1):
            display += '|'
            for num_count, num in enumerate(row, start=1):
                if num_count % 4 == 0:
                    display += f' {num:02} |'
                else:
                    display += f' {num:02} '
                if num_count % 16 == 0:
                    display += '\n'
                    if row_count % 4 == 0:
                        display += '+----------------+----------------+----------------+----------------+\n'
        return display

    def is_possible_solutions(self, y: int, x: int, n: int) -> bool:
        already_found = set()

        for i in range(16):
            already_found.add(self.board[y][i])
            already_found.add(self.board[i][x])

        sqr_y = (y//4)*4
        sqr_x = (x//4)*4
        for i in range(4):
            for j in range(4):
                already_found.add(self.board[sqr_y+i][sqr_x+j])

        return n not in already_found

    def find_empty(self) -> tuple or None:
        for y in range(16):
            for x in range(16):
                if self.board[y][x] == 0:
                    return (y,x)

    def solve(self) -> None:
        find = self.find_empty()
        if find:
            y, x = find
            for n in range(1,17):
                if self.is_possible_solutions(y,x,n):
                    self.board[y][x] = n
                    # self.solved_board = self.board
                    # print(self.__str__())
                    if self.solve():
                        return True
                    self.board[y][x] = 0
                    # self.solved_board = self.board
                    # print(self.__str__())
            return False
        self.solved_board = copy.deepcopy(self.board)
        return True

def main():

    board = [[ 0,15, 0, 1, 0, 2,10,14,12, 0, 0, 0, 0, 0, 0, 0],
             [ 0, 6, 3,16,12, 0, 8, 4,14,15, 1, 0, 2, 0, 0, 0],
             [14, 0, 9, 7,11, 3,15, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [ 4,13, 2,12, 0, 0, 0, 0, 6, 0, 0, 0, 0,15, 0, 0],
             [ 0, 0, 0, 0,14, 1,11, 7, 3, 5,10, 0, 0, 8, 0,12],
             [ 3,16, 0, 0, 2, 4, 0, 0, 0,14, 7,13, 0, 0, 5,15],
             [11, 0, 5, 0, 0, 0, 0, 0, 0, 9, 4, 0, 0, 6, 0, 0],
             [ 0, 0, 0, 0,13, 0,16, 5,15, 0, 0,12, 0, 0, 0, 0],
             [ 0, 0, 0, 0, 9, 0, 1,12, 0, 8, 3,10,11, 0,15, 0],
             [ 2,12, 0,11, 0, 0,14, 3, 5, 4, 0, 0, 0, 0, 9, 0],
             [ 6, 3, 0, 4, 0, 0,13, 0, 0,11, 9, 1, 0,12,16, 2],
             [ 0, 0,10, 9, 0, 0, 0, 0, 0, 0,12, 0, 8, 0, 6, 7],
             [12, 8, 0, 0,16, 0, 0,10, 0,13, 0, 0, 0, 5, 0, 0],
             [ 5, 0, 0, 0, 3, 0, 4, 6, 0, 1,15, 0, 0, 0, 0, 0],
             [ 0, 9, 1, 6, 0,14, 0,11, 0, 0, 2, 0, 0, 0,10, 8],
             [ 0,14, 0, 0, 0,13, 9, 0, 4,12,11, 8, 0, 0, 2, 0]]

    sudoku = Sudoku(board)
    sudoku.solve()
    print(sudoku)

if __name__ ==  '__main__':
    main()
