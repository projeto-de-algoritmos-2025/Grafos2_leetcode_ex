class Solution:
    def networkDelayTime(self, times, N, K):
        # Criação da lista de adjacência
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        # Heap de prioridade: (tempo acumulado, nó)
        min_heap = [(0, K)]
        dist = {}
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in dist:
                continue
            dist[node] = time
            for neighbor, weight in adj_list[node]:
                if neighbor not in dist:
                    heapq.heappush(min_heap, (time + weight, neighbor))
        
        if len(dist) != N:
            return -1
        return max(dist.values())