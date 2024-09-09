import sys
from collections import deque
input = sys.stdin.readline

v_num, e_num, init_v = map(int, input().split())

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 인접 노드 중 방문하지 않았던 노드를 재귀적으로 방문
    for near_v in graph[v]:
        if not visited[near_v]: 
            dfs(graph, near_v, visited)

#bfs
def bfs(graph, start, visited):
    #첫 번째 방문 노드 방문 처리
    queue = deque([start])
    visited[start] = True
    print()
    
    # 큐가 빌 때까지 반복
    while queue:
        # 노드를 꺼내면서 방문
        v = queue.popleft()
        print(v, end=' ')

        # 해당 노드의 인접 노드 중 방문하지 않은 노드들은 큐에 삽입하고 방문처리
        for near_v in graph[v]:
            if not visited[near_v]:
                queue.append(near_v)
                visited[near_v] = True

graph = [[] for _ in range (v_num+1)]
for i in range (e_num):
    v, near_v = map(int, input().split())
    graph[v].append(near_v)
    graph[near_v].append(v)

for i in range (1, v_num+1):
    graph[i].sort()

dfs_visited = [False] * (v_num+1)
bfs_visited = [False] * (v_num+1)

dfs(graph, init_v, dfs_visited)
bfs(graph, init_v, bfs_visited)
