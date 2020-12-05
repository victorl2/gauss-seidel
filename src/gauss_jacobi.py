from compressed_sparse_row import CSR
from numpy import zeros, concatenate, arange, copy

def jacobi(A,b,N=3,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Generate initial guess if needed                                                                                                                                                      
    if x is None:
        x = zeros(len(A[0]))
        
    matrix_a = CSR(A)
    result = zeros(matrix_a.size_rows)
    
    for _ in range(1, N+1):
        for i in range(matrix_a.size_rows):
            result[i] = b[i]
            for j in concatenate((arange(0, i), arange(i+1, matrix_a.size_rows))):
                result[i] -= matrix_a.get_value(i+1, j+1)*x[j]
            result[i] /= matrix_a.get_value(i+1, i+1)
        x = copy(result)
    return result