# 미래 도시

INF = int(1e9)

n, m = map(int, input().split()) # 회사의 개수와 경로의 개수 
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원 리스트 무한으로 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화 
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for j in range(m):
    a, b= map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# k번 회사를 방문한 뒤에 x번 회사로 가는 것
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
if (graph[1][k] + graph[k][x]) >= INF: 
    print(-1)
else:
    print(graph[1][k] + graph[k][x])

