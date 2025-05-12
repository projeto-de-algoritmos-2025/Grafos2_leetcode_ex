from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.components = size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False  # Already connected
        self.parent[root_a] = root_b
        self.components -= 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Anexar índice original a cada aresta
        for index, edge in enumerate(edges):
            edge.append(index)  # edge = [from, to, weight, index]

        # Ordenar arestas pelo peso
        edges.sort(key=lambda edge: edge[2])

        # Função para calcular o custo total da MST com inclusão/exclusão de arestas
        def kruskal(n, edges, include_edge=None, exclude_edge=None):
            uf = UnionFind(n)
            cost = 0
            if include_edge:
                f, t, w, _ = include_edge
                uf.union(f, t)
                cost += w
            for f, t, w, i in edges:
                if exclude_edge is not None and i == exclude_edge:
                    continue
                if uf.union(f, t):
                    cost += w
            return cost if uf.components == 1 else float('inf')

        # Custo mínimo da MST original
        min_mst_cost = kruskal(n, edges)

        critical = []
        pseudo_critical = []

        for f, t, w, i in edges:
            # Testa se a aresta é crítica (sua exclusão aumenta o custo)
            cost_without_edge = kruskal(n, edges, exclude_edge=i)
            if cost_without_edge > min_mst_cost:
                critical.append(i)
                continue

            # Testa se a aresta é pseudo-crítica (sua inclusão ainda leva ao mesmo custo)
            cost_with_edge = kruskal(n, edges, include_edge=[f, t, w, i])
            if cost_with_edge == min_mst_cost:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]
