from compressed_sparse_row import CSR
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot


def jacobi(A,b,N=25,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Generate initial guess if needed                                                                                                                                                      
    if x is None:
        x = zeros(len(A[0]))

    matrix_a = CSR(A)

    for iter in range(N):
        print("Iteration ", iter)
        for i in range(len(x)):
            R = []
            R.extend(x[0:i])
            R.extend(x[i:len(x)])

            aux_a = matrix_a.get_row(i+1)
            M = []
            M.extend(aux_a[0:i])
            M.extend(aux_a[i:len(x)])

            print(aux_a)
            print(M)
            print(R)

            new_value = (b[i] + dot(R,M))
            print(">x"+ str((i+1))," = ",  new_value)
            x[i] = new_value
    return x
    
A = array([[5,-1,2],[3,8,-2], [1,1,4]])
b = array([12,-25,6])
guess = array([0,0,0])

sol = jacobi(A,b,N=25,x=guess)

print("A:")
pprint(A)

print("b:")
pprint(b)

print("vetor solucao x:")
pprint(sol)
