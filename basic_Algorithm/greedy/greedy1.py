# 거슬러 줘야 할 돈이 N
# 동전의 종류가 K이면 시간 복잡도 O(K) 
# 탐욕법 가능한 이유: 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문

N = input()

def solutions(N):
    answer = 0
    coin = [500, 100, 50, 10]

    for i in range(len(coin)):
        answer += N // coin[i]
        N %= coin[i]
        
    return answer

print(solutions(1260))
