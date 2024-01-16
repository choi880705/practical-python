# bounce.py
#
# Exercise 1.5
"""
[page23 예제 프로그램]_V0_240116
고무 공을 100 미터 높이에서 떨어뜨린다. 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오른다. 공이 열 번 튈 동안, 그때마다 높이를 나타내는 테이블을 프린팅하는 프로그램 bounce.py를 작성하라.

1 : 100 * 0.6 = 60
2 :  60 * 0.6 = 36
3 :  36 * 0.6 = 21.6
...
변수 : 횟수(최대10), 떨높이, 0.6(튀는비율, 고정값), 튄높이, 소숫점 4자리까지 표시
"""
# 변수선언 및 초기화
height = 100  # 높이, 초기값 = 100m
BOUNCE_RATE = 0.6  # 바운스율 = 0.6(상수 변수는 대문자)
num_bounce = 0  # 바운스 횟수, 초기값 = 0

# wloop(height=100):
print(f"while문으로 만든것")
while num_bounce < 10:  # 10번 실행
    height *= BOUNCE_RATE  # 튄높이 = 떨높이 * 0.6
    num_bounce += 1  # 횟수 1 증가
    print(f"{num_bounce} 회 : {round(height, 4)}")  # 튄높이를 소숫점 4자리로 인쇄

print(f"for문으로 만든것")
# floop(height=100):
height = 100  # 높이, 초기값 = 100m
for num_bounce in range(1, 11):  # num_bounce가 1 ~ 10 동안 실행
    height *= BOUNCE_RATE  # 튄높이 = 떨높이 * 0.6
    print(f"{num_bounce} 회 : {round(height, 4)}")  # 튄높이를 소숫점 4자리로 인쇄


# wloop()
# floop()
print(f"끝났습니다")
print(f"줄맞춤해서 깔끔하게 보이게 만들어 보자")
print(f"for문을 사용해서 만들어 보자 -> 성공")
print(f"함수로 만들어 보자 -> 실패")
