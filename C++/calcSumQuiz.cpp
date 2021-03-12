# include <iostream>
# include <cassert>

int* calcSumQuiz(int mat1[], int mat2[], int rowSum[], int numCols){
    for(int i = 0; i < numCols; i++){
        rowSum[i] = mat1[i]+mat2[i];
    };
    return rowSum;
}

int main() {
    std::cout << "Testing...\n";

    int matrix[2][3] = {
        { 1, 2, 3 },
        { 4, 5, 6 }
    };

    int numRows = sizeof(matrix)/sizeof(*matrix);
    int numCols = sizeof(matrix[0])/sizeof(*matrix[0]);
    // calculate numRows and numCols using a general method.
    // DO NOT just set numRows = 2 and numCols = 3.
    // hint: use the size of the variable

    assert(numRows == 2);
    assert(numCols == 3);

    int rowSum[numCols];
    calcSumQuiz(matrix[0], matrix[1], rowSum, numCols);

    assert(rowSum[0] == 5);
    assert(rowSum[1] == 7);
    assert(rowSum[2] == 9);

    std::cout << "Success!";

    return 0;
}