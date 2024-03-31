from pysat.formula import IDPool, CNF
from pysat.solvers import Glucose4

import sys

form = 'P_{}_{}k{}'

k = int(sys.argv[1])
n = 3

if k == 1:
    # const value
    print("N = 2")
    exit(0)

while True:
    variables = IDPool()
    fromula_cnf = CNF()

    for x in range(n):
        for y in range(x):
            fromula_cnf.append([variables.id(form.format(x + 1, y + 1, c + 1)) for c in range(k)])

    for x in range(n):
        for y in range(x):
            for c in range(k):
                edge = -variables.id(form.format(x + 1, y + 1, c + 1))
                for c2 in range(c):
                    fromula_cnf.append([edge, -variables.id(form.format(x + 1, y + 1, c2 + 1))])

    for x in range(n):
        for y in range(x):
            for z in range(y):
                for c in range(k):
                    fromula_cnf.append([-variables.id(form.format(x + 1, y + 1, c + 1)), -variables.id(form.format(y + 1, z + 1, c + 1)), -variables.id(form.format(x + 1, z + 1, c + 1))])

    glSolver = Glucose4()
    glSolver.append_formula(fromula_cnf.clauses)

    if not glSolver.solve():
        print('N = ' + str(n - 1))
        break
    else:
        n = n + 1

    glSolver.delete()
