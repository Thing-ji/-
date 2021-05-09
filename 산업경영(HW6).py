from gurobipy import *
model = read('C:/Users/rlaek/.conda/pkgs/gurobi-9.1.1-py38_0/Doc/Gurobi/Data/exam1.lp')
model.optimize()
model.objval
model.printAttr("X")