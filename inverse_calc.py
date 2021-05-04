def GetCofactor(matrix, i, j):
	return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]


def DeterminantOfMatrix(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    elif len(matrix) == 2:
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]   
        return value

    determinant = 0
	# loop to traverse each column of matrix a.
    for current_column in range(len(matrix)):

		# calculating the sign corresponding
		# to co-factor of that sub matrix.
        sign = (-1) ** (current_column)

		# calling the function recursily to
		# get determinant value of
		# sub matrix obtained.
        sub_det = DeterminantOfMatrix(GetCofactor(matrix, 0, current_column))

		# adding the calculated determinant
		# value of particular column
		# matrix to total determinant.
        determinant += (sign * matrix[0][current_column] * sub_det)

    return determinant


def AdjointOfMatrix(matrix):
    n = len(matrix)
    adjoint_matrix = [[0] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            sign = 1 if (i+j)%2 == 0 else -1
            adjoint_matrix[j][i] = sign * DeterminantOfMatrix(GetCofactor(matrix, i, j))
    
    return adjoint_matrix


def InverseOfMatrix(matrix):
    n = len(matrix)
    adjoint_matrix = AdjointOfMatrix(matrix)
    determinant = DeterminantOfMatrix(matrix)
    inverse_matrix = [[0] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            current_element = 1 / determinant * adjoint_matrix[i][j]
            if (current_element.is_integer()):
                inverse_matrix[i][j] = int(current_element)
            else:
                inverse_matrix[i][j] = round(current_element, 2)
    
    return inverse_matrix


def PrintMatrix(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end='\t')
        print()


# * Driver code *
if __name__ == '__main__':
    # Enter Dimension & Little Talk
    n = int(input("Enter dimensions of square matrix. For ex: `3`: "))
    print(f"You are going to enter an {n}x{n} matrix:")

    # Initialize Matrix
    matrix = list()
    for i in range(n):
        matrix.append(list(map(int, input().split())))

	# printing determinant value
    print(f'Determinant of the {n}x{n} matrix is:', DeterminantOfMatrix(matrix))
    print(f'Inverse of the {n}x{n} matrix is:')
    PrintMatrix(InverseOfMatrix(matrix))

    input("Press any key to exit...")