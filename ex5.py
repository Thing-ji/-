from gutobipy import *

model = read('C:\Users\ADMIN\anaconda3\pkgs\gurobi-9.1.2-py38_0\Doc\Gurobi\Data\coins.lp')

model.optimize()

model.objval

model.printAttr('X')