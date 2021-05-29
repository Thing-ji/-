from gurobipy import *

m.Model('RAP')

R = ['Carlos', 'Joe', 'Monika']
J = ['Tester', 'JavaDeveloper', 'Architect']

# 직무적합도

combinations, ms = multidict({
    ('Carlos', 'Tester'):53,
    ('Carlos', 'JavaDeveloper'):27,
    ('Carlos', 'Architect'):13,
    ('Joe', 'Tester'):80,
    ('Joe', 'JavaDeveloper'):47,
    ('Joe', 'Architect'):67,
    ('Monika', 'Tester'):53,
    ('Monika', 'JavaDeveloper'):73,
    ('Monika', 'Architect'):47
})

# 2진 결정변수 생성
x = m.addVars(combinations, vtype=GRB.BINARY, name='assign')
# 직무 제약식
jobs = m.addConstrs((x.sum('*', j) == 1 for j in J), 'job')
# 직원 제약식
resources = m.addConstrs((x.sum(r, '*') <= 1 for r in R), 'resource')
# 목적함수
m.setObjective(x.prod(ms), GRB.MAXIMIZE)

m.write('RAP.lp')
m.optimize()

# 만약 최적해가 1개 이상 발견되면, 최적해를 출력
if m.Solcount>0:
    m.printAttr('x')

# 목적함수값 출력
print('total matching scores', m.objval)