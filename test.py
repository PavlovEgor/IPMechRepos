from scipy.optimize import minimize


fun = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2

bnds = ((0, None), (0, None))
cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
        {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
        {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})

res = minimize(fun, (2, 0), method='SLSQP', bounds=bnds,
               constraints=cons)

print(res.x)