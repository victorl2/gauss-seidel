from compressed_sparse_row import CSR
from pprint import pprint
from numpy import array, zeros, concatenate, arange, copy

def seidel(A,b,N=25,x=None):
    """Solves the equation Ax=b via the Seidel iterative method."""
    # Generate initial guess if needed                                                                                                                                                      
    if x is None:
        x = zeros(len(A[0]))
        
    matrix_a = CSR(A)
    result = copy(x)

    for _ in range(0, N):
        for i in range(matrix_a.size_rows):
            result[i] = b[i]
            for j in concatenate((arange(0, i), arange(i+1, matrix_a.size_rows))):
                result[i] -= matrix_a.get_value(i+1, j+1)*result[j]
            result[i] /= matrix_a.get_value(i+1, i+1)
    return result

A = array([[2.0,1.0],[8.0,-1.0]])
b = array([11.0, 29.0])
guess = array([0.0,0.0])

sol = seidel(A,b,N=25,x=guess)

print("A:")
pprint(A)

print("b:")
pprint(b)

print("vetor solucao x:")
pprint(sol)