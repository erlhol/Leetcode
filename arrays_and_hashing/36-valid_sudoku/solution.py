class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = dict()
        columns = dict()
        boxes = dict()

        for row in range(len(board)):
            for column in range(len(board[row])):
                num = board[row][column]

                if num == ".":
                    continue

                # Calculate the box number for the current cell
                box_num = (row // 3) * 3 + (column // 3) + 1

                # Initialize sets for rows, columns, and boxes if not present
                if row not in rows:
                    rows[row] = set()
                if column not in columns:
                    columns[column] = set()
                if box_num not in boxes:
                    boxes[box_num] = set()

                # Check if the number already exists in the current row, column, or box
                if num in rows[row] or num in columns[column] or num in boxes[box_num]:
                    return False

                # Add the number to the respective row, column, and box sets
                rows[row].add(num)
                columns[column].add(num)
                boxes[box_num].add(num)

        return True
