"""图论：岛屿、克隆图、课程表等。"""

from collections import deque
from typing import Optional

from algorithm.common.nodes import GraphNode


def num_islands(grid: list[list[str]]) -> int:
    """200. 岛屿数量"""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                count += 1
                dfs(i, j)
    return count


def clone_graph(node: Optional[GraphNode]) -> Optional[GraphNode]:
    """133. 克隆图"""
    if not node:
        return None
    cloned: dict[GraphNode, GraphNode] = {}

    def dfs(cur: GraphNode) -> GraphNode:
        if cur in cloned:
            return cloned[cur]
        copy = GraphNode(cur.val)
        cloned[cur] = copy
        for nei in cur.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node)


def course_schedule(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """207. 课程表"""
    graph: dict[int, list[int]] = {i: [] for i in range(num_courses)}
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    taken = 0
    while queue:
        node = queue.popleft()
        taken += 1
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return taken == num_courses


def course_schedule_ii(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """210. 课程表 II"""
    graph: dict[int, list[int]] = {i: [] for i in range(num_courses)}
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    order: list[int] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return order if len(order) == num_courses else []
