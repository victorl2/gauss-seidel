import sys, os
from numpy import array
from compressed_sparse_row import CSR

A = array([
                [10, -1, 0, 0, 0, 0, 0, 0, 0, 0],[4, 11, 0, 0, 1, 0, 0, 1, 0, 0],
                [1, 2, 12, 2, 0, 0, 3, 0, 0, 1], [0, 0, 0, 13, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 3, 14, 2, 0, -1, 2, 0], [0, 0, 0, 1, 0, 15, 2, 0, -2, 2],
                [0, 0, 0, 1, 0, 2, 16, 0, 2, 1],[0, 0, 0, 3, 2, 2, 0, 17, 2, 0],
                [0, 0, 0, 1, 0, 3, 2, 0, 18, 2], [0, 0, 0, 1, 0, 2, 4, 0, 2, 19]
            ])


def test_csr_should_have_correct_vector_via():
    csr = CSR(A)
    expected_via = [1,3,7,13,16,21,26,31,36,41]
    assert csr.v_ia == expected_via
    

def test_csr_should_have_correct_vector_vaa():
    csr = CSR(A)
    expected_vaa = [10, -1, 11, 4, 1, 1, 12, 1, 2, 2, 3, 1, 13, 1, 1, 14, 3, 2, -1, 2, 15, 1, 2, -2, 2, 16, 1, 2, 2, 1, 17, 3, 2, 2, 2, 18, 1, 3, 2, 2, 19, 1, 2, 4, 2]
    assert csr.v_aa == expected_vaa

def test_csr_should_have_correct_vector_vja():
    csr = CSR(A)
    expected_vja = [1, 2, 2, 1, 5, 8, 3, 1, 2, 4, 7, 10, 4, 5, 8, 5, 4, 6, 8, 9, 6, 4, 7, 9, 10, 7, 4, 6, 9, 10, 8, 4, 5, 6, 9, 9, 4, 6, 7, 10, 10, 4, 6, 7, 9]
    assert csr.v_ja == expected_vja

def test_csr_get_value_should_return_correct_information():
    csr = CSR(A)
    assert csr.get_value(10,10) == 19
    assert csr.get_value(1,1) == 10
    assert csr.get_value(8,5) == 2
    assert csr.get_value(2,3) == 0



