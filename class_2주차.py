boolVar, intVar, floatVar, strVar = True, 0, 0.0, ""
print(type(boolVar),type(intVar), type(floatVar), type(strVar))

def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

## 전역 변수 선언 부분 ##
hap = 0

## 메인 변수 선언 부분 ##
hap = plus(100, 200)
print('100과 200의 plus() 함수 결과는 #d' % hap)



list1 = []
list2 = []
value = 1

for i in range(0, 3):
    for k in range(0, 4):
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = [] # 다시 비워주기

for i in range(0, 3):
    for k in range(0, 4):
        print("%3d" % list2[i][k], end = " ") # 구분을 " "으로
    print(" ")