"""矩阵相关题目。"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """240. 搜索二维矩阵 II"""
    if not matrix:
        return False
    row, col = len(matrix) - 1, 0
    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] == target:
            return True
        if matrix[row][col] > target:
            row -= 1
        else:
            col += 1
    return False


def set_zeroes(matrix: list[list[int]]) -> None:
    """73. 矩阵置零"""
    if not matrix:
        return
    zero_rows, zero_cols = set(), set()
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    for i in zero_rows:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    for j in zero_cols:
        for i in range(len(matrix)):
            matrix[i][j] = 0


def rotate_image(matrix: list[list[int]]) -> None:
    """48. 旋转图像"""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()


def search_sorted_matrix(matrix: list[list[int]], target: int) -> bool:
    """74. 搜索二维矩阵"""
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // cols][mid % cols]
        if value == target:
            return True
        if value < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def spiral_order(matrix: list[list[int]]) -> list[int]:
    """54. 螺旋矩阵"""
    if not matrix:
        return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result: list[int] = []
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result


def is_valid_sudoku(board: list[list[str]]) -> bool:
    """36. 有效的数独"""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            ch = board[r][c]
            if ch == ".":
                continue
            box = (r // 3) * 3 + c // 3
            if ch in rows[r] or ch in cols[c] or ch in boxes[box]:
                return False
            rows[r].add(ch)
            cols[c].add(ch)
            boxes[box].add(ch)
    return True


def generate_matrix(n: int) -> list[list[int]]:
    """59. 螺旋矩阵 II"""
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            matrix[top][c] = num
            num += 1
        top += 1
        for r in range(top, bottom + 1):
            matrix[r][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                matrix[bottom][c] = num
                num += 1
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                matrix[r][left] = num
                num += 1
            left += 1
    return matrix
