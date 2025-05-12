class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_heap = [(0, 0)]  # (cost, point index)
        total_cost = 0
        points_connected = 0

        while points_connected < n:
            cost, u = heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += cost
            points_connected += 1

            for v in range(n):
                if not visited[v]:
                    x1, y1 = points[u]
                    x2, y2 = points[v]
                    new_cost = abs(x1 - x2) + abs(y1 - y2)
                    heappush(min_heap, (new_cost, v))

        return total_cost