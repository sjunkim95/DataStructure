# 랜덤 0~200 사이의 10개 난수 생성, 오름차순으로 정렬
# 삽입정렬 Insertion Sort

import random

def insertionSort(array):
    for end in range(1, len(array)):
        for current in range(end, 0, -1):
            if array[current - 1] < array[current]: # 오름차순
                array[current], array[current - 1] = array[current - 1], array[current]
    return array

# random.randint(0, 200) 0~200 사이의 난수 발생
random_array = [ random.randint(0, 200) for _ in range(10)]

print("정렬 전: ", random_array)
random_array = insertionSort(random_array)
print("정렬 후: ", random_array)