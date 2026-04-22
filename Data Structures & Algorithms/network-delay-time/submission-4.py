class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijikstra
        cost = [10**10 if x != k -1 else 0 for x in range(n)]
        graph = [[] for _ in range(n)]

        for u,v,p in times:
            graph[u-1].append([v-1,p])

        pq = [(0,k-1)]

        while len(pq) > 0:
            vertex_cost, smallest_cost_vertex = heapq.heappop(pq)
            print(vertex_cost,smallest_cost_vertex, pq)

            for adj_vertex, cost_to_adj_vertex in graph[smallest_cost_vertex]:
                # if adj_vertex == smallest_cost_vertex:
                #     continue

                total_cost_to_adj_vertex = vertex_cost + cost_to_adj_vertex

                if cost[adj_vertex] > total_cost_to_adj_vertex:
                    heapq.heappush( pq, (total_cost_to_adj_vertex, adj_vertex))
                    cost[adj_vertex] = total_cost_to_adj_vertex

        print(cost)
        return max(cost) if max(cost) != 10**10 else -1


        