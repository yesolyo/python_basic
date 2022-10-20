name=input("이름을 입력하세요:")
sac=int(input("음성 통화 시간(초)을 입력하세요:"))
data=int(input("데이터 사용량(MB)을 입력하세요:"))
print(name,"님의 이용 요금입니다:",12100+(1.98*sac)+(55*data))
