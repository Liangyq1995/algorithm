"""回溯算法独立函数。"""

from collections import deque


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
    queue: deque[str] = deque([s])
    visited = {s}
    found = False
    while queue:
        cur = queue.popleft()
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
    from data_structures.trie.trie import Trie

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


def combine(n: int, k: int) -> list[list[int]]:
    """77. 组合"""
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n - (k - len(path)) + 2):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result


def generate_parenthesis(n: int) -> list[str]:
    """22. 括号生成"""
    ans: list[str] = []

    def backtrack(path: list[str], left: int, right: int) -> None:
        if len(path) == 2 * n:
            ans.append("".join(path))
            return
        if left < n:
            path.append("(")
            backtrack(path, left + 1, right)
            path.pop()
        if right < left:
            path.append(")")
            backtrack(path, left, right + 1)
            path.pop()

    backtrack([], 0, 0)
    return ans


def letter_combinations(digits: str) -> list[str]:
    """17. 电话号码的字母组合"""
    if not digits:
        return []
    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    combination: list[str] = []
    combinations: list[str] = []

    def backtrack(index: int) -> None:
        if index == len(digits):
            combinations.append("".join(combination))
            return
        for letter in phone_map[digits[index]]:
            combination.append(letter)
            backtrack(index + 1)
            combination.pop()

    backtrack(0)
    return combinations


def combination_sum3(k: int, n: int) -> list[list[int]]:
    """216. 组合总和 III"""
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int], remain: int) -> None:
        if len(path) == k:
            if remain == 0:
                result.append(path[:])
            return
        for i in range(start, 10):
            if i > remain:
                break
            path.append(i)
            backtrack(i + 1, path, remain - i)
            path.pop()

    backtrack(1, [], n)
    return result


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """39. 组合总和"""
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int], remain: int) -> None:
        if remain == 0:
            result.append(path[:])
            return
        if remain < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remain - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    """40. 组合总和 II"""
    candidates = sorted(candidates)
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int], remain: int) -> None:
        if remain == 0:
            result.append(path[:])
            return
        if remain < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, remain - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


def subsets(nums: list[int]) -> list[list[int]]:
    """78. 子集"""
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    """90. 子集 II"""
    nums = sorted(nums)
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def _is_valid_ip_segment(s: str, start: int, end: int) -> bool:
    if start > end:
        return False
    if s[start] == "0" and start != end:
        return False
    num = 0
    for i in range(start, end + 1):
        if not s[i].isdigit():
            return False
        num = num * 10 + int(s[i])
        if num > 255:
            return False
    return True


def restore_ip_addresses(s: str) -> list[str]:
    """93. 复原 IP 地址"""
    result: list[str] = []

    def backtrack(start: int, dots: int, current: str) -> None:
        if dots == 3:
            if _is_valid_ip_segment(s, start, len(s) - 1):
                result.append(current + s[start:])
            return
        for i in range(start, len(s)):
            if _is_valid_ip_segment(s, start, i):
                backtrack(i + 1, dots + 1, current + s[start : i + 1] + ".")
            else:
                break

    backtrack(0, 0, "")
    return result


def partition(s: str) -> list[list[str]]:
    """131. 分割回文串"""
    result: list[list[str]] = []

    def backtrack(start: int, path: list[str]) -> None:
        if start == len(s):
            result.append(path[:])
            return
        for i in range(start, len(s)):
            segment = s[start : i + 1]
            if segment == segment[::-1]:
                path.append(segment)
                backtrack(i + 1, path)
                path.pop()

    backtrack(0, [])
    return result


def find_sub_sequences(nums: list[int]) -> list[list[int]]:
    """491. 非递减子序列"""
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        if len(path) >= 2:
            result.append(path[:])
        used: set[int] = set()
        for i in range(start, len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in used:
                continue
            used.add(nums[i])
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def permute(nums: list[int]) -> list[list[int]]:
    """46. 全排列"""
    result: list[list[int]] = []

    def backtrack(path: list[int]) -> None:
        if len(path) == len(nums):
            result.append([nums[i] for i in path])
            return
        for i in range(len(nums)):
            if i in path:
                continue
            path.append(i)
            backtrack(path)
            path.pop()

    backtrack([])
    return result


def permute_unique(nums: list[int]) -> list[list[int]]:
    """47. 全排列 II"""
    nums = sorted(nums)
    result: list[list[int]] = []
    used = [False] * len(nums)

    def backtrack(path: list[int]) -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result


def word_search_exist(board: list[list[str]], word: str) -> bool:
    """79. 单词搜索"""
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, index: int) -> bool:
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False
        board[r][c] = "*"
        found = (
            dfs(r - 1, c, index + 1)
            or dfs(r + 1, c, index + 1)
            or dfs(r, c - 1, index + 1)
            or dfs(r, c + 1, index + 1)
        )
        board[r][c] = word[index]
        return found

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    return False


def make_square(matchsticks: list[int]) -> bool:
    """473. 火柴拼正方形"""
    total = sum(matchsticks)
    if total % 4 != 0:
        return False
    side = total // 4
    matchsticks = sorted(matchsticks, reverse=True)
    sides = [0] * 4

    def backtrack(i: int) -> bool:
        if i == len(matchsticks):
            return sides[0] == sides[1] == sides[2] == sides[3] == side
        for j in range(4):
            if sides[j] + matchsticks[i] <= side:
                sides[j] += matchsticks[i]
                if backtrack(i + 1):
                    return True
                sides[j] -= matchsticks[i]
        return False

    return backtrack(0)
