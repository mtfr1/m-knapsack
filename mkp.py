import pulp


items = [1, 2, 3, 4]
values = {1:16, 2:19, 3:23, 4:28}
a = {1 : {1 : 2, 2 : 3000},
	 2 : {1 : 3, 2 : 3500},
	 3 : {1 : 4, 2 : 5100},
	 4 : {1 : 5, 2:  7200}}
b = {1 : 7, 2 : 10000}


item_ch = pulp.LpVariable.dicts("Item", items, 0, 1, pulp.LpBinary)


model = pulp.LpProblem("MKP", pulp.LpMaximize)

model += pulp.lpSum(values[j]*item_ch[j] for j in items)

for i in b:
	model += pulp.lpSum(a[j][i]*item_ch[j] for j in items) <= b[i]

solver = pulp.CPLEX_PY()
solver.buildSolverModel(model)
model.solverModel.parameters.timelimit.set(1800)


start_time = model.solverModel.get_time()
solver.callSolver(model)
end_time = model.solverModel.get_time()

instance_size =  len(items) + len(b)
time = end_time - start_time
best_sol = model.solverModel.solution.get_objective_value()
best_bound = model.solverModel.solution.MIP.get_best_objective()
gap = model.solverModel.solution.MIP.get_mip_relative_gap() * 100

print("Tamanho da instancia = %d" % instance_size)
print("Tempo gasto = %f" % time)
print("Melhor solucao = %f" % best_sol)
print("Melhor bound = %f" % best_bound)
print("Gap de otimalidade = %f" % gap)