from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)

    # 0. 먼저 원소들과 원래 위치를 함께 기억해요
    for i in range (len(priorities)):
        priorities[i] = [priorities[i], i]

    
    print(priorities)
    # 1. priorities 중에 가장 높은 것이 뭔지 알아야 됨
    priorities_sort = sorted(priorities, reverse=True)
    print(priorities_sort)
    
    # 1-1. 가장 높은 우선순위를 기억합시다
    top_idx = 0
    # 1-2. 몇 번째 실행되는지 카운트하는 변수를 만들어요₩ 
    count = 0
    # 2. priorities를 돌면서 우선순위별로 처리
    while len(priorities) > 0:
        # 현재 
        top_pri = priorities_sort[top_idx][0]
        print("현재 우선순위", top_pri)
        print("지금 맨 앞에 있는 원소", priorities[0])

        # 현재 element의 우선순위가 현재 우선순위와 동일한지 확인
        if priorities[0][0] == top_pri:
            print(f"{top_pri}와 {priorities[0][0]}는 같아요. \n우리가 찾고 있는 우선순위예요.")
            print(f"{priorities[0]}을 pop할래요.")
            count += 1
            top_idx += 1

            if priorities[0][1] == location:
                return count
            priorities.popleft()
            
            
        else:
            print(f"{top_pri}와 {priorities[0][0]} 은 같지 않아요. \n우리가 찾고 있는 우선순위가 아니예요.")
            print(f"{priorities[0]}을 pop하고 뒤로 다시 줄서게 할래요.")
            # 우선순위가 높지 않다면 큐에서 뽑고
            elem = priorities.popleft()
            # 다시 뒤로 줄서게 합니다
            priorities.append(elem)
            
        print("count", count)
        print("현재", priorities) 
        print("--------------------------------------------\n")
    return count


def main():
    a = [1, 1, 9, 1, 1, 1]
    loc = 0
    print("최종 count", solution(a, loc))

main()

