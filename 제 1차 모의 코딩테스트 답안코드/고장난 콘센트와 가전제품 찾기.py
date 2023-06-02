UNKNOWN = 0
NORMAL = 1
BROKEN = 2

def solution(n, m, queries):
    sockets = [UNKNOWN for _ in range(n + 1)]
    products = [UNKNOWN for _ in range(m + 1)]

    # 정상 작동하는 콘센트와 가전 제품 확정하기
    for socket_id, product_id, is_working in queries:
        if is_working == 1:                 # 정상 작동이라면, 콘센트와 가전 제품 모두 정상임이 확정
            sockets[socket_id] = NORMAL
            products[product_id] = NORMAL
    
    # 비정상인 콘센트와 가전 제품 확정하기
    for socket_id, product_id, is_working in queries:
        if is_working == 0:  # 고장났다면,
            if sockets[socket_id] == NORMAL and products[product_id] == NORMAL:     # 모순된 상황
                return [-1, -1]
            
            if sockets[socket_id] == NORMAL:  # 콘센트가 정상이라면, 가전 제품이 고장임이 확정
                products[product_id] = BROKEN

            elif products[product_id] == NORMAL:  # 가전 제품이 정상이라면, 콘센트가 고장임이 확정
                sockets[socket_id] = BROKEN
            
    # 모순 검증하기
    for socket_id, product_id, is_working in queries:
        if is_working == 1:
            if sockets[socket_id] != NORMAL or products[product_id] != NORMAL:  # 둘 중 하나라도 고장이면 모순
                return [-1, -1]
        
        if is_working == 0:
            if sockets[socket_id] == NORMAL and products[product_id] == NORMAL:  # 둘 다 정상이면 모순
                return [-1, -1]
    
    # 정답 계산하기
    answer = [0, 0]
    for i in range(1, n + 1):
        if sockets[i] == NORMAL:
            answer[0] += 1
        if sockets[i] == BROKEN:
            answer[1] += 1
            
        
    for i in range(1, m + 1):
        if products[i] == NORMAL:
            answer[0] += 1
        if products[i] == BROKEN:
            answer[1] += 1
    
    return answer
