from compressed_sparse_row import CSR
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot


def jacobi(A,b,N=3,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Generate initial guess if needed                                                                                                                                                      

    matrix_a = CSR(A)
    new_solution = []

    for iter in range(N):
        print("Iteration ", iter)
        for i in range(len(x)):
            R = []
            R.extend(x[0:i])
            R.extend(x[i+1:len(x)])

            aux_a = matrix_a.get_row(i+1)
            M = []
            M.extend(aux_a[0:i])
            M.extend(aux_a[i+1:len(x)])

            new_value = (b[i] + dot(R,M))/aux_a[i]

            print('sum:', b[i], R, M,'divide', aux_a[i] , ' = ', new_value)
            print(10*'#')
            new_solution.append(new_value)
        x = [value for value in new_solution]
        new_solution = []
    return x
    
A = array([[2.0, 1.0],[8.0,-1]])
b = array([11.0,29.0])
guess = [0.0,0.0]

sol = jacobi(A,b,N=25,x=guess)

print("A:")
pprint(A)

print("b:")
pprint(b)

print("vetor solucao x:")
pprint(sol)
