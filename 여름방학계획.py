from gurobipy import *

'''

<2021 여름방학 공부계획 짜기>
다음과 같은 과목과 주어진 제약에서 가치를 최대로 하는 최적화 모델링 수립하기

                 영어  Python  SQL  정보처리기사  SQLD  빅데이터분석기사  공모전
상대적 가치         5      2     3       3        2          1         1   
예상 할애 시간       4      3     2       2        1          3         3

하루 할애 가능시간: 8시간
과목 선택 -> 1, 그렇지 않으면 -> 0

'''

n = 7
V = [5, 2, 3, 3, 2, 1, 1]
T = [4, 3, 2, 2, 1, 3, 3]
c = 8

m = Model()

# 결정변수 생성
x = m.addVars(n, vtype=GRB.BINARY, name='x')
# 목적함수 생성
m.setObjective(quicksum(x[i]*V[i] for i in range(n)), GRB.MAXIMIZE)
# 제약식 생성
m.addConstr(quicksum(x[i]*T[i] for i in range(n)) <= c, name = 'Time')

m.optimize()

if m.SolCount > 0:
    m.printAttr('X')

print('THE BEST VALUE OF SUBJECT: ', m.objval)

m.write('summer_vacation_study_plan.lp')