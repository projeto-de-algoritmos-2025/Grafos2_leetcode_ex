import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Criar grafo direcionado com pesos
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Fila de prioridade: (tempo acumulado, nó atual)
        min_heap = [(0, k)]
        shortest_time = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in shortest_time:
                continue
            shortest_time[node] = time
            for neighbor, weight in graph[node]:
                if neighbor not in shortest_time:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        # Se nem todos os nós foram alcançados, retorna -1
        if len(shortest_time) != n:
            return -1

        # Retorna o tempo máximo necessário para alcançar todos os nós
        return max(shortest_time.values())
