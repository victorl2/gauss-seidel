from numpy import array

# Structure that allow storage of matrix with CSR compression
# The index for values starts at 1
class CSR:
    def __init__(self, matrix):
        self.size_rows = len(matrix[0])
        self.size_cols = len(matrix)
        self.parse_matrix(matrix)

    def get_value(self, row, col):
        if row > self.size_rows or col > self.size_cols or col <= 0 or row <= 0:
            raise Exception("O valor posicao "+ str((row,col)) + " nao esta presente na matriz")
        start_pos = self.v_ia[row - 1] -1
        end_pos = len(self.v_aa) if row >= self.size_rows else self.v_ia[row] - 1
        
        for i in range(start_pos, end_pos):
            if self.v_ja[i] == col:
                return self.v_aa[i]
        return 0
    
    def get_row(self, row):
        return [self.get_value(row,i) for i in range(1, self.size_cols)]

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
