from numpy import array
from compressed_sparse_row import CSR
from gauss_jacobi import jacobi
from gauss_seidel import seidel

A1 = array([
                [10, -1, 0, 0, 0, 0, 0, 0, 0, 0],[4, 11, 0, 0, 1, 0, 0, 1, 0, 0],
                [1, 2, 12, 2, 0, 0, 3, 0, 0, 1], [0, 0, 0, 13, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 3, 14, 2, 0, -1, 2, 0], [0, 0, 0, 1, 0, 15, 2, 0, -2, 2],
                [0, 0, 0, 1, 0, 2, 16, 0, 2, 1],[0, 0, 0, 3, 2, 2, 0, 17, 2, 0],
                [0, 0, 0, 1, 0, 3, 2, 0, 18, 2], [0, 0, 0, 1, 0, 2, 4, 0, 2, 19]
            ])
b1 = array([9.0, 17.0, 21.0, 15.0, 20.0, 18.0, 2.0, 28.0, 26.0, 28.0])
x1 = array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    
A2 = array([[5.0, -2.0, 3.0],[-3.0, 9.0, 1.0],[2.0, -1.0, -7.0]])
b2 = array([-1.0, 2.0, 3.0])
x2 = array([0.0, 0.0, 0.0])

def test_csr_should_have_correct_vector_via():
    csr = CSR(A1)
    expected_via = [1,3,7,13,16,21,26,31,36,41]
    assert csr.v_ia == expected_via
    

def test_csr_should_have_correct_vector_vaa():
    csr = CSR(A1)
    expected_vaa = [10, -1, 11, 4, 1, 1, 12, 1, 2, 2, 3, 1, 13, 1, 1, 14, 3, 2, -1, 2, 15, 1, 2, -2, 2, 16, 1, 2, 2, 1, 17, 3, 2, 2, 2, 18, 1, 3, 2, 2, 19, 1, 2, 4, 2]
    assert csr.v_aa == expected_vaa

def test_csr_should_have_correct_vector_vja():
    csr = CSR(A1)
    expected_vja = [1, 2, 2, 1, 5, 8, 3, 1, 2, 4, 7, 10, 4, 5, 8, 5, 4, 6, 8, 9, 6, 4, 7, 9, 10, 7, 4, 6, 9, 10, 8, 4, 5, 6, 9, 9, 4, 6, 7, 10, 10, 4, 6, 7, 9]
    assert csr.v_ja == expected_vja

def test_csr_get_value_should_return_correct_information():
    csr = CSR(A1)
    assert csr.get_value(10,10) == 19
    assert csr.get_value(1,1) == 10
    assert csr.get_value(8,5) == 2
    assert csr.get_value(2,3) == 0

def test_jacobi_a1():
    jacobi = jacobi(A1, b, N=25, x= x1)
     assert jacobi == []

def test_seidel_a1():
    seidel = seidel(A1, b, N=25, x= x1)
    assert seidel == []

def test_jacobi_a2():
    jacobi = jacobi(A2, b2, N=3, x= x2)
     assert jacobi == []

def test_seidel_a2():
    seidel = seidel(A2, b2, N=3, x= x2)
    assert seidel == []