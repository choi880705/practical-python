'''
[p.17/예제 프로그램 해석]
어느 날 아침, 당신은 시카고의 시어스 타워 (Sears tower) 근처를 거닐다가 보도에 1 달러 지폐를 한장 올려뒀다.
그 후 매일 외출할 때마다 그 위에 지폐를 얹어 탑을 쌓으며, 높이는 매일 두 배로 불어난다.
돈으로 쌓은 탑의 높이가 시어스 타워의 높이와 같아지려면 시간이 얼마나 걸릴까?
'''

#sears.py
bill_thickness=0.11*0.001 #지폐의 두께를 미터로 환산
sears_height=442 #높이(미터)
num_bills=1 #지폐의 수 초기값
day=1 #일자

while num_bills*bill_thickness<sears_height: #while문-(지폐의 수*지폐의 두께)가 시어스 타워의 높이보다 작을 동안 반복
    print(day, num_bills, num_bills*bill_thickness) #일자, 일자별 지폐의 수, (일자별 지폐의 수*지폐의 두께)를 출력
    day=day+1 #일자는 하루씩 증가
    num_bills=num_bills*2 #지폐는 두 배씩 증가
print('Number of days', day) #Number of days와 결과의 마지막 일자 출력
print('Number of bills', num_bills) #Number of bills와 결과의 마지막 지폐의 수 출력
print('Final height', num_bills*bill_thickness) #Final height와 (결과의 마지막 지폐의 수*지폐의 두께)를 출력