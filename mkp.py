import numpy as np
import pulp

# model
def mkp(items, values, a, b):
	model = pulp.LpProblem("MKP", pulp.LpMaximize)

	item_ch = pulp.LpVariable.dicts("Item", items, 0, 1, pulp.LpBinary)
	model += pulp.lpSum(values[j]*item_ch[j] for j in items) #objective function
	
	for i in b:
		model += pulp.lpSum(a[j][i]*item_ch[j] for j in items) <= b[i] #constraints

	return model

n_tests = int(input())
for _ in range(n_tests):
	n, m, opt = map(float, input().split())
	n, m = int(n), int(m)

	items = [i for i in range(n)]

	pj = list(map(float, input().split()))
	values = {}	
	for j in range(n):
		values[j] = pj[j]

	a = {}
	matrix = []
	for i in range(m):
		line = list(map(int, input().split()))
		matrix.append(line)
	
	matrix = np.array(matrix)
	matrix = matrix.T

	for i in range(n):
		constraint = {}
		for j in range(m):
			constraint[j] = matrix[i][j]
		a[i] = constraint

	bi = list(map(float, input().split()))
	b = {}
	for i in range(m):
		b[i] = bi[i]


	model = mkp(items, values, a, b)

	solver = pulp.CPLEX_PY()
	solver.buildSolverModel(model)
	model.solverModel.parameters.timelimit.set(1800)


	start_time = model.solverModel.get_time()
	solver.callSolver(model)
	end_time = model.solverModel.get_time()

	n = str(len(items))
	m = str(len(b))
	if _ == 0:
		tightness = "0.25"
	elif _ == 1:
		tightness = "0.5"
	else:
		tightness = "0.75"
	time = str(end_time - start_time)
	best_sol = str(model.solverModel.solution.get_objective_value())
	best_bound = str(model.solverModel.solution.MIP.get_best_objective())
	gap = str(model.solverModel.solution.MIP.get_mip_relative_gap() * 100)

	# print("Tamanho da instancia = %d" % instance_size)
	# print("Tempo gasto = %f" % time)
	# print("Melhor solucao = %f" % best_sol)
	# print("Melhor bound = %f" % best_bound)
	# print("Gap de otimalidade = %f" % gap)

	with open('results.csv', 'a') as f:
		f.write(n +","+ m + "," + tightness + "," +
    			time + "," + best_sol + "," + best_bound + "," +
    			gap + "\n")

		
