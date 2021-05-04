#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

vector <vector <int>> Initialize2DVector(int, int);
void Print2DVector(vector <vector <int>>);
void GetCofactor(vector <vector <int>>&, vector <vector <int>> &, int, int);
int DeterminantOfSquareMatrix(vector <vector <int>>&);
void InverseUsingAdjugate(vector <vector <int>>);


// Main function
int main(int argc, char *argv[]) {
    /* ------Getting Dimensions of Matrix------ */
    // Ask For Info
    cout << "Enter dimensions of square matrix. For ex: `3`" << '\n';
    int dimension;
    cin >> dimension;
    // Confirm Matrix Information
    cout << "You are going to enter an " << dimension << "x" << dimension << " square " << "matrix:" << '\n';

    /* ------Enter & Get Matrix------ */
    // Define Vector
    vector <vector <int>> matrix = Initialize2DVector(dimension, dimension);
    // Ask for elements
    for (int i = 0; i < dimension; i++) {
        for (int j = 0; j < dimension; j++) {
            cin >> matrix[i][j];
        }
    }
    // Print Matrix for Confirmation
    cout << "You entered this " << dimension << "x" << dimension << " square " << "matrix:" << '\n';
    Print2DVector(matrix);

    /* ------Calculate Inverse of  Matrix------ */
    cout << "The determinant of " << dimension << "x" << dimension << " square " << "matrix is: " << DeterminantOfSquareMatrix(matrix) << '\n';
}


/* ------Reusable & Logic Functions------ */
// Create 2 Dimensional Vector and Resize
vector <vector <int>> Initialize2DVector(int row, int column) {
    //! It assumes the column size in each row is the same
    vector <vector <int>> twoDimVector(row);
    // Resize child vectors
    for (int i = 0; i < row; i++) {
        twoDimVector[i].resize(column);
    }
    // Return
    return twoDimVector;
}

// Printing 2 Dimensional Vector
void Print2DVector(vector <vector <int>> twoDimVector) {
    //! It assumes the column size in each row is the same
    int row = twoDimVector.size();
    int column = twoDimVector[0].size();
    // Iterate over elements
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            cout << twoDimVector[i][j] << '\t';
        }
        cout << '\n';
    }
}

// Recursive Function for Finding The Determinant of Square Matrix
int DeterminantOfSquareMatrix(vector <vector <int>> &matrix) {
    int dimension = matrix.size();
    int determinant = 0;
    // Base Cases
    if (dimension == 1)
        return matrix[0][0];
    else if (dimension == 2)
        return ((matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1]));
    else {
        vector <vector <int>> submatrix = Initialize2DVector(dimension, dimension);
        Print2DVector(submatrix);
        for (int x = 0; x < dimension; x++) {
            int subi = 0;
            for (int i = 1; i < dimension; i++) {
                int subj = 0;
                for (int j = 0; j < dimension; j++) {
                    if (j == x)
                        continue;
                    submatrix[subi][subj] = matrix[i][j];
                    subj++;
                }
                subi++;
            }
            determinant += (pow(-1, x) * matrix[0][x] * DeterminantOfSquareMatrix(submatrix));
        }
    }

    return determinant;
}

// Inverse of  Matrix using Adjugate
void InverseUsingAdjugate(vector <vector <int>> matrix) {

}


/* ------Other Details------ */
// Ask for dimensions
// Then Get Input
// Then Print Given
// Then Print Inverse of Matrix

/*
* [Input Example]
1 1 -1
1 0 1
2 1 1
* [Output Example]
*/
/*
* [Input Example]
1 0 2 -1
3 0 0 5
2 1 4 -3
1 0 5 0
* [Output Example]
30
*/

/*
    // Function to get cofactor of mat[p][q] in temp[][]. n is
// current dimension of mat[][]
void GetCofactor(vector <vector <int>>  &matrix, vector <vector <int>> &submatrix, int p, int q) {
    int dimension = submatrix.size();
    int i = 0, j = 0;
    // Looping for each element of the matrix
    for (int row = 0; row < dimension; row++) {
        for (int col = 0; col < dimension; col++) {
            //  Copying into submatrix only those
            //  element which are not in given row and
            //  column
            if (row != p && col != q) {
                submatrix[i][j++] = matrix[row][col];
                // Row is filled, so increase row index and
                // reset col index
                if (j == dimension - 1){
                    j = 0;
                    i++;
                }
            }
        }
    }
    Print2DVector(submatrix);
}
    */