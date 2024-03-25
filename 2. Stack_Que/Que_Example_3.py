# 지하철 관제 프로그램
# 차고지 ------> 강남역 ------> 역삼역 ------> 선릉역 ------> 삼성역
# 전차A, 전차B, 전차C

def deQueue(stationNo):
   front = -1       # 출구 인덱스
   rear = -1        # 입구 인덱스
   
   # 해당 역 입구 인덱스 구하기
   for i in line_2[stationNo]:
       if i != None:
           rear += 1                    # 만약에 전차가 존재하면 입구의 인덱스 +1 증가

   # 가장 앞에 있는 데이터 추출
   front += 1
   Train = line_2[stationNo][front]     # 출발한 전차 이름
   line_2[stationNo][front] = None      # 출발 후 None 값으로
   print(Train, "전차가 출발 했습니다. ")

   # 추출 후 한칸씩 당기기
   for i in range(front+1, rear+1):
       line_2[stationNo][i-1] = line_2[stationNo][i]
       line_2[stationNo][i] = None

    # 현재 역에서 추출된 데이터를 다음 역에 추가
   enQueue(Train, stationNo)
   return

def enQueue(Train, stationNo):
    rear = -1        # 입구 인덱스

    # 해당 역 인덱스에 데이터 추가
    if stationNo+1 == 5:  # 마지막 역이면 첫번째 역으로 이동
        # 해당 역 입구 인덱스 구하기
        for i in line_2[0]:
            if i != None:
                rear += 1
        rear += 1
        line_2[0][rear] = Train
    else:
        # 해당 역 입구 인덱스 구하기
        for i in line_2[stationNo+1]:
            if i != None:
                print("현재 rear값", rear)
                rear += 1
                print("다음 rear 값", rear)
        rear += 1
        print("마지막 rear값", rear)
        
        line_2[stationNo+1][rear] = Train

    return
    

def station_print():
    print("차고지의 전차 항목: ", line_2[0])
    print("강남역 차고지의 전차 항목: ", line_2[1])
    print("역삼역 차고지의 전차 항목: ", line_2[2])
    print("선릉역 차고지의 전차 항목: ", line_2[3])
    print("삼성역 차고지의 전차 항목: ", line_2[4])


garage = ["전차A", "전차B", "전차C"]
gangnam = [ None, None, None ]
yeoksam = [ None, None, None ]
seolleung  = [ None, None, None ]
samsung = [ None, None, None ]
line_2 = [garage, gangnam, yeoksam, seolleung, samsung] # 2차원 리스트

while True:
    station_print()
    select = int(input("출발신호: 0. 차고지 1. 강남역  2. 역삼역 3. 선릉역 4. 삼성역: "))
    if select == 0:
        print("차고지에 가장 앞에 있는 전차 출발!! ")
        deQueue(select)

    elif select == 1:
        print("강남역에 도착한 전차 출발")
        deQueue(select)
        
    elif select == 2:
        print("역삼역에 도착한 전차 출발")
        deQueue(select)

    elif select == 3:
        print("선릉역에 도착한 전차 출발")
        deQueue(select)

    elif select == 4:
        print("삼성역에 도착한 전차 출발")
        deQueue(select)

    else:
        print("알 수 없는 번호입니다.")
