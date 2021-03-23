import random
import time

def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary) - 1
    count = 0
    
    while (start <= end):
        count += 1
        mid = (start + end) // 2
        if fData == ary[mid]:
            print(count, '회 검색에 성공함')
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return pos

## 전역 변수부
dataAry = []
findData = 0

dataAry = [random.randint(0, 1000) for _ in range(3000)]
print('정렬전 -->', dataAry)

dataAry.sort()
findData = random.randint(0, 1000)
print('정렬후 -->', dataAry)
start_time = time.time()

position = binSearch(dataAry, findData)
end_time = time.time()
if position == -1:
    print(findData, '(이)가 없네요.')
else:
    print(findData, '은 ', position, '위치에 있음.')
print("계산시간은", end_time-start_time)