from gurobipy import *

n = 7
p = [6, 5, 8, 9, 6, 7, 3]
w = [2, 3, 6, 7, 5, 9, 4]
c = 9

# 모델 생성
m = Model()

# 변수 생성
x = m.addVars(n, vtype = GRB.BINARY, name = 'x')

# 목적함수 생성
m.setObjective(quicksum(x[i] * p[i] for i in range(n)), GRB.MAXIMIZE)

# 제약식 생성
m.addConstr(quicksum(x[i] * w[i] for i in range(n))<=c, name = 'knapsack')

# 모델 최적화
m.optimize()

# 최적해 발견
if m.Solcount > 0:
    m.printAttr('x')

m.write('knapsack.lp')