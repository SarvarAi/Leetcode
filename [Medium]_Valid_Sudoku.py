from typing import List, Dict

class Solution:
    def _check_row(self, row):
        for r in row:
            if r == '.':
                pass
            else:
                if row.count(r) != 1:
                    return False
        return True

    def _check_column(self, board):
        index = 0

        while index < len(board):
            temp = []
            for r in board:
                temp.append(r[index])
            col = self._check_row(temp)
            if col:
                pass
            else:
                return False
            index += 1
        return True

    def _check_box(self, board):
        index = 0 
        while index < len(board):
            row1 = board[index]
            row2 = board[index+1]
            row3 = board[index+2]

            first_box = [row1[0], row1[1], row1[2], row2[0], row2[1], row2[2], row3[0], row3[1], row3[2]]
            second_box = [row1[3], row1[4], row1[5], row2[3], row2[4], row2[5], row3[3], row3[4], row3[5]]
            third_box = [row1[6], row1[7], row1[8], row2[6], row2[7], row2[8], row3[6], row3[7], row3[8]]


            validate1 = self._check_row(first_box) 
            validate2 = self._check_row(second_box)
            validate3 = self._check_row(third_box)

            print(third_box)
            print(validate3)

            if validate1 and validate2 and validate3:
                pass
            else:
                return False

            index += 3
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_val = self._check_column(board)
        boxs_val = self._check_box(board)

        for row in board:
            if not self._check_row(row):
                return False
        if not (column_val and boxs_val):
            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    test_row_1 = [".",".",".",".","8",".",".","7","9"]

    test_board_1 = [   ["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]

    test_board_2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]

    test_board_3 = [
    [".","2",".",".",".",".",".",".","."],
    [".",".",".",".",".",".","5",".","1"],
    [".",".",".",".",".",".","8","1","3"],
    ["4",".","9",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".","2",".",".",".",".",".","."],
    ["7",".","6",".",".",".",".",".","."],
    ["9",".",".",".",".","4",".",".","."],
    [".",".",".",".",".",".",".",".","."]
    ]
    print(sol.isValidSudoku(test_board_3))
    print(sol._check_row(['.', '.', '.', '5', '.', '1', '8', '1', '3']))
