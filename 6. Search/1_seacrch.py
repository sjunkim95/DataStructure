"""
    검색=탐색( 정렬 있는 상태 vs 정렬이 없는 상태 )
        1. 순차 검색 : 순서대로 저장되어 있는 자료를 처음부터 끝까지 순서대로 검색
            1. 정렬이 없는 상태에서 가능 (정렬 X, 정렬이 없어도 된다)
            2. 속도 많이 느림
        2. 이진(이분) 검색 : 가운데에 있는 항목을 비교해서 크면 오른쪽 작으면 왼쪽 검색
            1. 퀵 정렬 유사
            2. 정렬이 되어 있는 상태에서 가능 (정렬 O, 정렬이 필요하다)
            3. 순차검색보다는 효율성이 좋다
        3. 이진 트리 검색 : 이진트리(3.Tree_Graph)를 이용한 검색 방법
            1. 검색이 단순하다
            2. 삽입과 삭제 과정이 존재하기 때문에 복잡하다
        4. 해시 함수 = 해싱 검색 : 키가 있는 위치를 계산하여 바로 찾아가는 검색 방식
            1. 해싱 함수 사용
"""