def full_house(cnt: list) -> bool:
    joker = cnt[0]  # 현재 가진 조커의 개수

    for two_num in range(1, 14):        # 2장으로 구성할 카드의 번호
        for three_num in range(1, 14):  # 3장으로 구성할 카드의 번호
            if two_num == three_num:    # 서로 다른 카드여야 한다는 조건 확인하기
                continue

            need_joker_for_pair = max(0, 2 - cnt[two_num])              # 2장 구성에 필요한 조커 개수
            need_joker_for_triple = max(0, 3 - cnt[three_num])          # 3장 구성에 필요한 조커 개수
            need_joker = need_joker_for_pair + need_joker_for_triple    # 필요한 조커의 총 개수

            if joker >= need_joker:
                return True
    
    return False


def solution(cards):
    cnt = [0 for _ in range(14)]  # cnt[i] := i 가 적힌 카드의 개수
    ans = 0
    for c in cards:
        cnt[c] += 1

        if full_house(cnt):  # 현재 가진 카드들로 full house를 만들 수 있는 지 판단하기
            ans += 1
            cnt = [0 for _ in range(14)]
    
    return ans
