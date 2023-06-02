def solution(s):
    answer = 0

    cnt = [0 for _ in range(5)]
    for x in s:
        cnt[x] += 1
    
    # 4명 그룹은 택시 배정
    answer = cnt[4]

    # 3명 그룹도 택시 배정
    answer += cnt[3]
    cnt[1] -= min(cnt[1], cnt[3])  # 1명 그룹을 최대한 배정

    # 2명 그룹은 서로 합쳐서 배정
    answer += cnt[2] // 2
    cnt[2] %= 2  # 짝이 되지 않는 2명 그룹 개수 구하기

    # 남은 그룹을 택시에 배정
    left = cnt[1] + cnt[2] * 2  # 남아있는 총 사람 수
    answer += left // 4         # 4명씩 택시 부르기
    if left % 4 != 0:           # 남은 사람들이 있다면, 택시 하나 더 부르기
        answer += 1

    return answer
