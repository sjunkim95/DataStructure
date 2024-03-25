from operator import itemgetter # 외부 라이브러리 가져오기 : itemgetter 메소드

# 책이름과 저자별 정렬 함수
def makeIndex(array, pos):  # 인수: 배열, 정렬기준
    beforeArray = []    # 
    index = 0
    for data in array:
        beforeArray.append((data[pos], index))
        index += 1
    
    sortedArray = sorted(beforeArray, key=itemgetter(0)) # sorted(배열명, key=itemgetter(인덱스번호) : 해당 인덱스 기준으로 정렬 
    return sortedArray                                                                                          # (즉, 책 또는 저자 이름으로 정렬하겠다)
    
# 이진검색
def bookSearch(array, fdata):
    pos = -1
    start = 0
    end = len(array) - 1
    while (start <= end):
        mid = (start + end) // 2
        if fdata == array[mid][0]:
            return array[mid][1]
        elif fdata > array[mid][0]:
            start = mid + 1
        else:
            end = mid - 1
    return pos

# 전역변수
# 책 이름, 저자
bookArray = [
    ['어린왕자', '쌩덱쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'],
    ['신곡', '단테'], ['돈키호테', '세르반테스'], ['동물농장', '조지오웰'],
    ['데미안', '헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅']
]

nameIndex = [ ]     # 책이름
nameIndex = makeIndex(bookArray, 0)
print("정렬 후: ", nameIndex) 

authIndex = [ ]    # 저자이름
authIndex = makeIndex(bookArray, 1)
print("정렬 후: ", authIndex) 

btn = int(input("검색 카테고리 ( 1. 책이름  2. 저자이름 입력: )"))

findname = ''
if btn == 1:
    findname = input("책이름: ")
    findpos = bookSearch(nameIndex, findname)
    if findpos == -1:
        print(findname + '의 도서는 없습니다.')
    else:
        print(findname,'의 도서는', findpos,'위치에 있습니다')
elif btn == 2:
    findname = input("저자이름: ")
    findpos = bookSearch(nameIndex, findname)
    if findpos == -1:
        print(findname + '의 도서는 없습니다.')
    else:
        print(findname,'의 도서는', findpos,'위치에 있습니다')
else:
    print("알 수 없는 번호입니다.")