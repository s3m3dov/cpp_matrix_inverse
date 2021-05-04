import unittest, time
from inverse_calc import GetCofactor, DeterminantOfMatrix, AdjointOfMatrix, InverseOfMatrix


class TestGetCofactor(unittest.TestCase):
    def testSquareMatrix_3(self):
        square_matrix_3 = [[1, 1, -1], [1, 0, 1], [2, 1, 1]]
        cofactor_of_0_0 = [[0, 1], [1, 1]] 
        self.assertEqual(GetCofactor(square_matrix_3, 0, 0), cofactor_of_0_0, f"Should be {cofactor_of_0_0}")


class TestDeterminant(unittest.TestCase):
    def testSquareMatrix_1(self):
        square_matrix_1 = [[3]]
        self.assertEqual(DeterminantOfMatrix(square_matrix_1), 3, "Should be 3")

    def testSquareMatrix_2(self):
        square_matrix_2 = [[3, 5], [2, 1]]
        self.assertEqual(DeterminantOfMatrix(square_matrix_2), -7, "Should be -7")
    
    def testSquareMatrix_3(self):
        square_matrix_3 = [[1, 1, -1], [1, 0, 1], [2, 1, 1]]
        self.assertEqual(DeterminantOfMatrix(square_matrix_3), -1, "Should be -1")

    def testSquareMatrix_4a(self):
        square_matrix_4a = [[1, 0, 2, -1], [3, 0, 0, 5], [2, 1, 4, -3], [1, 0, 5, 0]]
        self.assertEqual(DeterminantOfMatrix(square_matrix_4a), 30, "Should be 30")

    def testSquareMatrix_4b(self):
        square_matrix_4b = [[1, 1, 1, -1], [1, 0, 1, 0], [2, 1, 2, 1], [1, 0, 0, 1]]
        self.assertEqual(DeterminantOfMatrix(square_matrix_4b), -2, "Should be -2")


class TestAdjointOfMatrix(unittest.TestCase):
    def testSquareMatrix_2(self):
        square_matrix_2 = [[3, 5], [2, 1]]
        adjoint_matrix_2 = [[1, -5], [-2, 3]]
        self.assertEqual(AdjointOfMatrix(square_matrix_2), adjoint_matrix_2, f"Should be {adjoint_matrix_2}")
    
    def testSquareMatrix_3(self):
        square_matrix_3 = [[1, 1, -1], [1, 0, 1], [2, 1, 1]]
        adjoint_matrix_3 = [[-1, -2, 1], [1, 3, -2], [1, 1, -1]]
        self.assertEqual(AdjointOfMatrix(square_matrix_3), adjoint_matrix_3, f"Should be {adjoint_matrix_3}")

    def testSquareMatrix_4(self):
        square_matrix_4 = [[1, 0, 2, -1], [3, 0, 0, 5], [2, 1, 4, -3], [1, 0, 5, 0]]
        adjoint_matrix_4 = [[25, 5, 0, -10], [-75, 3, 30, 6], [-5, -1, 0, 8], [-15, 3, 0, 6]]
        self.assertEqual(AdjointOfMatrix(square_matrix_4), adjoint_matrix_4, f"Should be {adjoint_matrix_4}")


class TestInverseOfMatrix(unittest.TestCase):
    def testSquareMatrix_2(self):
        square_matrix_2 = [[3, 5], [2, 1]]
        inverse_matrix_2 = [[-0.14, 0.71], [0.29, -0.43]]
        self.assertEqual(InverseOfMatrix(square_matrix_2), inverse_matrix_2, f"Should be {inverse_matrix_2}")
    
    def testSquareMatrix_3(self):
        square_matrix_3 = [[1, 1, -1], [1, 0, 1], [2, 1, 1]]
        inverse_matrix_3 = [[1, 2, -1], [-1, -3, 2], [-1, -1, 1]]
        self.assertEqual(InverseOfMatrix(square_matrix_3), inverse_matrix_3, f"Should be {inverse_matrix_3}")

    def testSquareMatrix_4(self):
        square_matrix_4 = [[1, 0, 2, -1], [3, 0, 0, 5], [2, 1, 4, -3], [1, 0, 5, 0]]
        inverse_matrix_4 = [[0.83, 0.17, 0, -0.33], [-2.5, 0.1, 1, 0.2], [-0.17, -0.03, 0, 0.27], [-0.5, 0.1, 0, 0.2]]
        self.assertEqual(InverseOfMatrix(square_matrix_4), inverse_matrix_4, f"Should be {inverse_matrix_4}")


# Baby Driver :D
if __name__ == '__main__':
    unittest.main()