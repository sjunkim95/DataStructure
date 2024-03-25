"""
    정렬: sort: 자료들을 순서대로 나열 [ 내림차순 : DESC, 오름차순: ASC ]
        1. 정렬된 데이터들은 검색 빠르다
        2. 종류
            1. 선택 정렬 [ select sort ]
                * 여러 데이터들 중에서 가장 작은 값을 뽑는 작동을 반복하여 값 정렬 한다
                * 최소값을 찾아서 순서대로 새로운 곳에 배치
                    172 180 163 153 190                     153
                    172 180 190                             153 163
                    180 190                                 153 162 172
                    190                                     153 162 172 180
                                                            153 162 172 180 190
                * 교환 방식
                172 180 163 153 190                         172 > 180 False
                172 180 163 153 190                         172 > 163 True      163 172 180 153 190
                163 172 180 153 190                         163 > 153 True      153 163 172 180 190
                153 163 172 180 190                         153 > 190 False

            2. 삽입 정렬 [ Insertion sort ]
                * 기존 데이터들 중에서 자신의 위치를 찾아 데이터를 삽입하는 정렬
                172 180 163 153 190                     172
                172 180 163 153 190                     172 180 (172보다 작으면 왼쪽, 크면 오른쪽에 정렬)
                172 180 163 153 190                     163 172 180
                172 180 163 153 190                     153 163 172 180
                172 180 163 153 190                     153 163 172 180 190

            3. 버블 정렬 [ Bubble sort ]
                * 첫 번째 값부터 시작해서 바로 앞뒤 데이터를 비교하여 큰 것은 뒤로 보내는 방식
                * 이미 정렬된 상태에서 중간에 데이터 추가 후 재정렬시 (제일 빠르다)
                '150' 170 100 160                         150 170 100 160 (150 -> 170과 비교)
                150 '170' 100 160                         150 100 170 160 (170 -> 150(앞), 100(뒤) 와 비교)
                150 170 '100' 160                         150 100 160 170

            4. 퀵 정렬 [ Quick sort ]
                * 기준[pirot]을 선정하는 첫 과정 -> 기준은 중간에 위치한 값 선정
                * 기준 기준으로 왼쪽: 작은값 / 오른쪽: 큰값
                * 데이터가 많으면 많을수록 다른 정렬보다 빠르다 (정렬되기 전 상태에서는 퀵이 버블정렬보다 빠르다)
                172 180 163 153 190                 기준 : 163
                153 163 172 180 190                 
"""

# 삽입정렬은 본인이 어디다 삽입할건지 찾는 과정이 중요하다
# 선택정렬은 최솟값을 찾는게 중요하다
# 퀵정렬은 중간값 찾아서, 재귀를 사용하는 것이 중요