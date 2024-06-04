#!/usr/bin/python3
# coding=utf-8
import heapq


class Solution:
    def __init__(self):
        self.inf = 5000
        self.G = [[0, 5, 2, 100, 100, 100, 100],
                  [5, 0, 100, 1, 6, 100, 100],
                  [2, 100, 0, 6, 100, 8, 100],
                  [100, 1, 6, 0, 1, 2, 100],
                  [100, 6, 100, 1, 0, 100, 7],
                  [100, 100, 8, 2, 100, 0, 3],
                  [100, 100, 100, 100, 7, 3, 0]]
        self.neighbormap = {}
        self.init_neighbormap()
        self.check_neighbor_output()

    def init_neighbormap(self):
        for i in range(len(self.G)):
            flag = False
            for j in range(len(self.G[i])):
                if flag == False and self.G[i][j] < 100 and self.G[i][j] != 0:
                    self.neighbormap[i] = [j]
                    flag = True
                elif self.G[i][j] < 100 and self.G[i][j] != 0:
                    self.neighbormap[i].append(j)
                else:
                    continue
        print("init neighbormap success!")

    def check_neighbor_output(self):
        print("输出节点及其邻居：")
        for key, value in self.neighbormap.items():
            print("key =", key, "value =", value)

    def dijkstra(self):
        n = len(self.G)  # 图的顶点数量
        result = []
        
        for source in range(n):
            dist = [self.inf] * n  # 存储源点到各个顶点的最短距离
            visited = [False] * n  # 标记顶点是否被访问过
            dist[source] = 0  # 源点到自身的距离为0
            
            # 创建一个优先队列，按照距离的增序排列，每个元素存储距离和顶点编号
            pq = [(0, source)]
            heapq.heapify(pq)
            
            while pq:
                u_dist, u = heapq.heappop(pq)

                if visited[u]:
                    continue
                
                visited[u] = True  # 将顶点标记为已访问
                
                # 遍历与顶点u相邻的顶点
                for v in range(n):
                    if self.G[u][v] != 0 and not visited[v]:
                        new_dist = dist[u] + self.G[u][v]  # u到v的距离
                        
                        if new_dist < dist[v]:
                            dist[v] = new_dist  # 更新最短距离
                            heapq.heappush(pq, (dist[v], v))  # 将v加入优先队列
            result.append(dist)
        # 使用softmax对每一行进行归一化
        for i in range(len(result)):
            row = result[i]
            sumexp = sum(row)
            row[:] = [-(value / sumexp) for value in row]
        return result

    def computeQ_getpath(self, cliplim, dis, startnode):
        n = len(cliplim[0])
        m = len(dis)
        print(n)
        print(m)
        Q = [[-self.inf] * m for _ in range(n + 1)]
        path = []
        maximun = -self.inf
        maxindex = 0

        for i in range(m):
            Q[0][i] = dis[startnode][i]
            if maximun < dis[startnode][i]:
                maximun = dis[startnode][i]
                maxindex = i

        visited = set()
        que = [maxindex]

        for i in range(1, n + 1):
            que.append(maxindex)
            visited.add(maxindex)

            while que:
                nodev = que.pop(0)
                Q[i][nodev] = max(Q[i][nodev], Q[i - 1][nodev] + cliplim[nodev][i - 1])
                neighbor = self.neighbormap[nodev]

                for neighbor_k in neighbor:
                    Q[i][nodev] = max(Q[i][nodev], Q[i][neighbor_k] + dis[nodev][neighbor_k])
                    if neighbor_k not in visited:
                        que.append(neighbor_k)
                        visited.add(neighbor_k)

            maximun = -self.inf
            for k in range(m):
                if maximun < Q[i][k]:
                    maximun = Q[i][k]
                    maxindex = k

            if len(visited) == m:
                print("Q数组第", i, "行计算成功！本次循环使Q取得最大值的节点为-----", maxindex)
                path.append(maxindex)
            visited.clear()

        print("检查计算的Q值：")
        for row in Q:
            print(*("{:.4f}".format(x) for x in row))
        return path

cliplim = [[0.1, 0.1, 0.05, 0.025],
           [0.4, 0.1, 0.05, 0.025],
           [0.1, 0.1, 0.1, 0.025],
           [0.1, 0.4, 0.05, 0.025],
           [0.1, 0.1, 0.6, 0.05],
           [0.1, 0.1, 0.05, 0.8],
           [0.1, 0.1, 0.1, 0.05]]
s = Solution()
dis = s.dijkstra()
path = s.computeQ_getpath(cliplim, dis, 0)

# 检查dis是否正确初始化，Q计算是否正确
print("输出距离代价矩阵：")
for row in dis:
    print(*("{:.4f}".format(x) for x in row))