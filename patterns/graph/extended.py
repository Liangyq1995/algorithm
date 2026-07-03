"""图论扩展：BFS/DFS/并查集等。"""

from collections import deque, defaultdict
from typing import Optional

import heapq


def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    """127. 单词接龙"""
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    queue = deque([(begin_word, 1)])
    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return steps
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                nxt = word[:i] + c + word[i + 1 :]
                if nxt in word_set:
                    word_set.remove(nxt)
                    queue.append((nxt, steps + 1))
    return 0


def solve_surrounded_regions(board: list[list[str]]) -> None:
    """130. 被围绕的区域"""
    if not board:
        return
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
            return
        board[r][c] = "T"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(rows):
        dfs(i, 0)
        dfs(i, cols - 1)
    for j in range(cols):
        dfs(0, j)
        dfs(rows - 1, j)
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "T":
                board[i][j] = "O"


def longest_increasing_path(matrix: list[list[int]]) -> int:
    """329. 矩阵中的最长递增路径"""
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    memo: dict[tuple[int, int], int] = {}

    def dfs(r: int, c: int) -> int:
        if (r, c) in memo:
            return memo[(r, c)]
        best = 1
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                best = max(best, 1 + dfs(nr, nc))
        memo[(r, c)] = best
        return best

    return max(dfs(r, c) for r in range(rows) for c in range(cols))


def calc_equation(
    equations: list[list[str]], values: list[float], queries: list[list[str]]
) -> list[float]:
    """399. 除法求值"""
    graph: dict[str, dict[str, float]] = defaultdict(dict)
    for (a, b), val in zip(equations, values):
        graph[a][b] = val
        graph[b][a] = 1 / val

    def dfs(start: str, end: str, visited: set[str]) -> float:
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)
        for nei, weight in graph[start].items():
            if nei in visited:
                continue
            if nei == end:
                return weight
            result = dfs(nei, end, visited)
            if result != -1.0:
                return weight * result
        return -1.0

    answers: list[float] = []
    for a, b in queries:
        answers.append(dfs(a, b, set()))
    return answers


def is_bipartite(graph: list[list[int]]) -> bool:
    """785. 判断二分图"""
    color = [-1] * len(graph)
    for start in range(len(graph)):
        if color[start] != -1:
            continue
        queue = deque([start])
        color[start] = 0
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if color[nei] == -1:
                    color[nei] = 1 - color[node]
                    queue.append(nei)
                elif color[nei] == color[node]:
                    return False
    return True


def find_cheapest_price(
    n: int, flights: list[list[int]], src: int, dst: int, k: int
) -> int:
    """787. K 站中转内最便宜的航班"""
    prices = [float("inf")] * n
    prices[src] = 0
    for _ in range(k + 1):
        temp = prices[:]
        for u, v, w in flights:
            if prices[u] != float("inf"):
                temp[v] = min(temp[v], prices[u] + w)
        prices = temp
    return -1 if prices[dst] == float("inf") else int(prices[dst])


def all_paths_source_target(graph: list[list[int]]) -> list[list[int]]:
    """797. 所有可能的路径"""
    target = len(graph) - 1
    result: list[list[int]] = []

    def dfs(node: int, path: list[int]) -> None:
        if node == target:
            result.append(path[:])
            return
        for nei in graph[node]:
            path.append(nei)
            dfs(nei, path)
            path.pop()

    dfs(0, [0])
    return result


def num_buses_to_destination(routes: list[list[int]], source: int, target: int) -> int:
    """815. 公交路线"""
    if source == target:
        return 0
    stop_to_routes: dict[int, list[int]] = defaultdict(list)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].append(i)
    queue = deque([(source, 0)])
    visited_stops = {source}
    visited_routes: set[int] = set()
    while queue:
        stop, buses = queue.popleft()
        for route_idx in stop_to_routes[stop]:
            if route_idx in visited_routes:
                continue
            visited_routes.add(route_idx)
            for nxt in routes[route_idx]:
                if nxt == target:
                    return buses + 1
                if nxt not in visited_stops:
                    visited_stops.add(nxt)
                    queue.append((nxt, buses + 1))
    return -1


def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    """841. 钥匙和房间"""
    visited: set[int] = set()

    def dfs(room: int) -> None:
        visited.add(room)
        for key in rooms[room]:
            if key not in visited:
                dfs(key)

    dfs(0)
    return len(visited) == len(rooms)


def update_board(board: list[list[str]], click: list[int]) -> list[list[str]]:
    """529. 扫雷游戏"""
    rows, cols = len(board), len(board[0])
    r, c = click

    def count_mines(cr: int, cc: int) -> int:
        total = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "M":
                    total += 1
        return total

    def dfs(cr: int, cc: int) -> None:
        if board[cr][cc] == "M":
            board[cr][cc] = "X"
            return
        mines = count_mines(cr, cc)
        board[cr][cc] = "B" if mines == 0 else str(mines)
        if mines == 0:
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "E":
                        dfs(nr, nc)

    if board[r][c] == "M":
        board[r][c] = "X"
    else:
        dfs(r, c)
    return board


def oranges_rotting(grid: list[list[int]]) -> int:
    """994. 腐烂的橘子"""
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while queue:
        r, c, minutes = queue.popleft()
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, minutes + 1))
    return minutes if fresh == 0 else -1


def get_skyline(buildings: list[list[int]]) -> list[list[int]]:
    """218. 天际线问题"""
    events: list[tuple[int, int, int]] = []
    for left, right, height in buildings:
        events.append((left, -height, right))
        events.append((right, height, 0))
    events.sort()
    result: list[list[int]] = []
    heap: list[tuple[int, int]] = [(0, float("inf"))]
    for x, neg_h, right in events:
        while heap[0][1] <= x:
            heapq.heappop(heap)
        if neg_h < 0:
            heapq.heappush(heap, (neg_h, right))
        max_h = -heap[0][0]
        if not result or result[-1][1] != max_h:
            result.append([x, max_h])
    return result
