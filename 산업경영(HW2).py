def calcul(num1, num2):
    sum = num1 + num2
    mul = num1 * num2
    sha = num1 // num2
    rest = num1 % num2
    squa = num1 ** num2

    return print(sum, mul, sha, rest, squa)

num1 = int(input('첫 번째 정수입력\n')) # 100 입력
num2 = int(input('두 번째 정수입력\n')) # 20 입력

calcul(num1, num2)


