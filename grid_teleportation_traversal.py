from typing import List
from collections import defaultdict
from queue import Queue


def is_portal(cell):
    return 'A' <= cell <= 'Z'

def not_wall(cell):
    return cell != '#'

def get_portals(matrix):
    portals = defaultdict(list)

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if is_portal(cell):
                portals[cell].append((i, j))

    return portals

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        delta = ((0, -1), (0, 1), (-1, 0), (1, 0))
        portals = get_portals(matrix)
        q = Queue()
        q.put((-1, 0, -1))
        visited = [[False]*cols for _ in range(rows)]

        while not q.empty():
            dist, r, c = q.get()

            for dr, dc in delta:
                i = r + dr
                j = c + dc

                if 0 <= i < rows and 0 <= j < cols:
                    cell = matrix[i][j]
                    if not_wall(cell) and not visited[i][j]:
                        if i == rows - 1 and j == cols - 1:
                            return dist + 1
                        if is_portal(cell):
                            for k, l in portals[cell]:
                                if k == rows - 1 and l == cols - 1:
                                    return dist + 1
                                q.put((dist + 1, k, l))
                                visited[k][l] = True
                            del portals[cell]
                        else:
                            q.put((dist + 1, i, j))
                            visited[i][j] = True

        return -1


m = [".","#"]
print(Solution().minMoves(m))
