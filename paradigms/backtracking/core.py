"""回溯算法独立函数。"""


def solve_n_queens(n: int) -> list[list[str]]:
    """51. N 皇后"""
    result: list[list[str]] = []
    cols: set[int] = set()
    diag1: set[int] = set()
    diag2: set[int] = set()
    board = [["."] * n for _ in range(n)]

    def backtrack(row: int) -> None:
        if row == n:
            result.append(["".join(line) for line in board])
            return
        for col in range(n):
            if col in cols or row - col in diag1 or row + col in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col] = "Q"
            backtrack(row + 1)
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result


def remove_invalid_parentheses(s: str) -> list[str]:
    """301. 删除无效的括号"""
    def is_valid(text: str) -> bool:
        balance = 0
        for ch in text:
            if ch == "(":
                balance += 1
            elif ch == ")":
                balance -= 1
                if balance < 0:
                    return False
        return balance == 0

    result: set[str] = set()
    queue = [s]
    visited = {s}
    found = False
    while queue:
        cur = queue.pop(0)
        if is_valid(cur):
            result.add(cur)
            found = True
        if found:
            continue
        for i in range(len(cur)):
            if cur[i] not in "()":
                continue
            nxt = cur[:i] + cur[i + 1 :]
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return list(result)


def total_n_queens(n: int) -> int:
    """52. N 皇后 II"""
    count = 0
    cols: set[int] = set()
    diag1: set[int] = set()
    diag2: set[int] = set()

    def backtrack(row: int) -> None:
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col in cols or row - col in diag1 or row + col in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            backtrack(row + 1)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return count


def solve_sudoku(board: list[list[str]]) -> None:
    """37. 解数独"""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty: list[tuple[int, int]] = []
    for r in range(9):
        for c in range(9):
            ch = board[r][c]
            if ch == ".":
                empty.append((r, c))
            else:
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[(r // 3) * 3 + c // 3].add(ch)

    def backtrack(index: int) -> bool:
        if index == len(empty):
            return True
        r, c = empty[index]
        box = (r // 3) * 3 + c // 3
        for digit in map(str, range(1, 10)):
            if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                continue
            board[r][c] = digit
            rows[r].add(digit)
            cols[c].add(digit)
            boxes[box].add(digit)
            if backtrack(index + 1):
                return True
            board[r][c] = "."
            rows[r].remove(digit)
            cols[c].remove(digit)
            boxes[box].remove(digit)
        return False

    backtrack(0)


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    """212. 单词搜索 II"""
    from algorithm.data_structures.trie.trie import Trie

    trie = Trie()
    for word in words:
        trie.insert(word)
    rows, cols = len(board), len(board[0])
    result: set[str] = set()

    def dfs(r: int, c: int, node: Trie, path: str) -> None:
        ch = board[r][c]
        if ch not in node.children:
            return
        node = node.children[ch]
        path += ch
        if node.is_end:
            result.add(path)
        board[r][c] = "#"
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, node, path)
        board[r][c] = ch

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie, "")
    return list(result)
