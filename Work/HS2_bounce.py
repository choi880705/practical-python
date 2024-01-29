'''
[p.23/연습 문제 1.5 얌체공 풀이]
고무 공을 100 미터 높이에서 떨어뜨린다. 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오른다.
공이 열 번 튈 동안, 그때마다 높이를 나타내는 테이블을 프린팅하는 프로그램 bounce.py를 작성하라.
'''

#bounce.py
height=100 #높이의 초기값
num_bounce=0 #튀어오르는 횟수 초기값

for num_bounce in range(0, 10): #for문-1회부터 10회까지의 범위 동안 반복 실행
    height=height*3/5 #기존 높이의 3/5만큼 튀어오른다
    num_bounce=num_bounce+1 #튀어오르는 횟수는 1씩 증가
    print(num_bounce, round(height, 4)) #튀어오르는 횟수와 튀어오르는 높이(소수점 4자리까지) 출력
    
'''
! num_bounce의 초기값을 1로 설정하고 range 범위를 (1, 11)로 설정할 경우 튀어오르는 횟수가 2~11로 출력됨....!!!

num_bounce=1로, range(1, 11)로 설정하고 실행했을 때
[ChatGPT 설명]
코드에서 num_bounce=num_bounce+1라인이 있습니다.
따라서 for 루프 안에서 이미 range(1, 11)로 정의된 num_bounce가 반복문 안에서 1씩 증가합니다.
그래서 각 반복에서 num_bounce는 range에 정의된 값보다 1씩 큰 값이 됩니다.
'''


##for문 이하 내용 순서를 바꿔서 작성
height=100 #높이의 초기값
num_bounce=1 #튀어오르는 횟수 초기값

for num_bounce in range(1, 11): #for문-1회부터 10회까지의 범위 동안 반복 실행
    height=height*3/5 #기존 높이의 3/5만큼 튀어오른다
    print(num_bounce, round(height, 4)) #튀어오르는 횟수와 튀어오르는 높이(소수점 4자리까지) 출력
    num_bounce=num_bounce+1 #튀어오르는 횟수는 1씩 증가

'''
num_bounce=1로, range(1, 11)로 설정
print의 위치가 'num_bounce=num_bounce+1'보다 뒤에 올 경우 num_bounce의 초기값이 아닌 초기값+1부터 출력된다는 것을 확인함
'''