from numpy import array, zeros, diag, diagflat, dot

# Structure that allow storage of matrix with CSR compression
# The index for values starts at 1
class CSR:
    def __init__(self, matrix):
        self.size_rows = len(matrix[0])
        self.size_cols = len(matrix)
        self.parse_matrix(matrix)

    def get_value(self, row, col):
        if row > self.size_rows or col > self.size_cols :
            raise Exception("O valor posicao acessada nao esta presente na matriz")
        start_pos = self.v_ia[row - 1] -1
        end_pos = len(self.v_aa) if row >= self.size_rows else self.v_ia[row] - 1
        
        for i in range(start_pos, end_pos):
            if self.v_ja[i] == col:
                return self.v_aa[i]
        return 0

    def get_dimmension(self):
        return (self.size_rows, self.size_cols)
    
    def parse_matrix(self, matrix):
        """ Generates the optimazed storage with V_aa, V_ja and V_ia vectors"""
        self.v_aa = [] # values
        self.v_ja = [] # columns
        self.v_ia = [] # lines

        for i in range(self.size_rows):
            self.v_ia.append(len(self.v_aa) + 1)
            if matrix[i][i] != 0:
                self.v_aa.append(matrix[i][i])
                self.v_ja.append(i + 1)
            for j in range(self.size_cols):
                if matrix[i][j] != 0 and i != j:
                    self.v_aa.append(matrix[i][j])
                    self.v_ja.append(j + 1)
    
def validation():
    A = array([
                [10, -1, 0, 0, 0, 0, 0, 0, 0, 0],[4, 11, 0, 0, 1, 0, 0, 1, 0, 0],
                [1, 2, 12, 2, 0, 0, 3, 0, 0, 1], [0, 0, 0, 13, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 3, 14, 2, 0, -1, 2, 0], [0, 0, 0, 1, 0, 15, 2, 0, -2, 2],
                [0, 0, 0, 1, 0, 2, 16, 0, 2, 1],[0, 0, 0, 3, 2, 2, 0, 17, 2, 0],
                [0, 0, 0, 1, 0, 3, 2, 0, 18, 2], [0, 0, 0, 1, 0, 2, 4, 0, 2, 19]
            ])
    csr = CSR(A)

    expected_via = [1,3,7,13,16,21,26,31,36,41]
    expected_vja = [1, 2, 2, 1, 5, 8, 3, 1, 2, 4, 7, 10, 4, 5, 8, 5, 4, 6, 8, 9, 6, 4, 7, 9, 10, 7, 4, 6, 9, 10, 8, 4, 5, 6, 9, 9, 4, 6, 7, 10, 10, 4, 6, 7, 9]
    expected_vaa = [10, -1, 11, 4, 1, 1, 12, 1, 2, 2, 3, 1, 13, 1, 1, 14, 3, 2, -1, 2, 15, 1, 2, -2, 2, 16, 1, 2, 2, 1, 17, 3, 2, 2, 2, 18, 1, 3, 2, 2, 19, 1, 2, 4, 2]
    if csr.v_aa != expected_vaa:
        print("V_aa:", csr.v_aa)
        raise Exception("V_aa CSR matrix is invalid")
    if csr.v_ia != expected_via:
        print("V_ia:", csr.v_ia)
        raise Exception("V_ia CSR matrix is invalid")
    if csr.v_ja != expected_vja:
        print("V_ja:", csr.v_ia)
        raise Exception("V_ja CSR matrix is invalid")
    
    if csr.get_value(10,10) != 19:
        raise Exception("Wrong value at pos (10,10) should be 19, is", csr.get_value(10,10))
    if csr.get_value(1,1) != 10:
        raise Exception("Wrong value at pos (1,1) should be 10, is", csr.get_value(1,1))
    if csr.get_value(8,5) != 2:
        raise Exception("Wrong value at pos (8,5) should be 2, is", csr.get_value(8,5))
    if csr.get_value(2,3) != 0:
        raise Exception("Wrong value at pos (2,3) should be 0, is", csr.get_value(2,3))

    print("Everything is as expected !!")

if __name__ == "__main__":
    validation()

